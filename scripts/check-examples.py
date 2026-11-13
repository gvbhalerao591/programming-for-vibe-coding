"""Check teaching API behaviour and learner archive using only Python's stdlib."""

import csv
import importlib.util
import json
from pathlib import Path
import tempfile
from threading import Thread
import unittest
from urllib.error import HTTPError
from urllib.request import Request, build_opener, ProxyHandler
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


example = load_module("course_example", ROOT / "episodes/files/serve.py")
packaging = load_module("course_packaging", ROOT / "scripts/package-examples.py")


class QuietHandler(example.CourseHandler):
    def log_message(self, *_args):
        pass


class TeachingExamples(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.database = Path(self.temporary.name) / "practice.sqlite3"
        self.start_server()
        self.addCleanup(self.stop_server)
        self.client = build_opener(ProxyHandler({}))

    def start_server(self):
        example.initialise_database(self.database)
        self.server = example.ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
        self.server.database = self.database
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def request(self, path="/api/activities", body=None, raw=None, content_type="application/json"):
        data = json.dumps(body).encode() if body is not None else raw
        request = Request(self.base + path, data=data,
                          headers={"Content-Type": content_type})
        try:
            response = self.client.open(request, timeout=5)
        except HTTPError as error:
            response = error
        with response:
            payload = response.read()
            if "application/json" in response.headers.get("Content-Type", ""):
                payload = json.loads(payload)
            return response.status, payload

    def test_seed_records_match_both_topic_three_formats(self):
        status, records = self.request()
        self.assertEqual(status, 200)
        self.assertEqual(records, json.loads(example.SEED.read_text()))
        with (ROOT / "episodes/data/activities.csv").open(newline="") as source:
            csv_records = list(csv.DictReader(source))
        self.assertEqual(len(csv_records), len(records))
        for csv_record, record in zip(csv_records, records):
            self.assertEqual(csv_record["activity"], record["activity"])
            self.assertEqual(int(csv_record["id"]), record["id"])
            self.assertEqual(float(csv_record["hours"]), record["hours"])
            self.assertEqual(csv_record["completed"] == "true", record["completed"])

    def test_saved_record_is_retrievable_after_server_restart(self):
        status, saved = self.request(body={"activity": " Read methods ", "hours": 1.5})
        self.assertEqual(status, 201)
        self.assertEqual(saved["activity"], "Read methods")
        self.assertIs(saved["completed"], False)
        self.assertIsInstance(saved["id"], int)
        self.assertIn(saved, self.request()[1])
        self.stop_server()
        self.start_server()
        records = self.request()[1]
        self.assertEqual(len(records), 4)
        self.assertIn(saved, records)

    def test_rejected_inputs_never_create_records(self):
        before = self.request()[1]
        invalid = [
            {"activity": "   ", "hours": 1},
            {"activity": "", "hours": 1},
            {"activity": "Work", "hours": 0},
            {"activity": "Work", "hours": 24.1},
            {"activity": "Work", "hours": "1.5"},
            {"activity": "Work", "hours": True},
            {"activity": "Work", "hours": None},
            {"activity": "Work", "hours": float("nan")},
            {"activity": "Work", "hours": float("inf")},
            {"activity": "Work", "hours": 10 ** 1000},
            {"hours": 1}, ["not a record"],
        ]
        for value in invalid:
            with self.subTest(value=repr(value)[:100]):
                status, response = self.request(body=value)
                self.assertEqual(status, 400)
                self.assertIn("error", response)
        self.assertEqual(self.request()[1], before)

    def test_numeric_boundaries_and_malformed_requests(self):
        for hours in (0.001, 24):
            self.assertEqual(self.request(body={"activity": "Work", "hours": hours})[0], 201)
        self.assertEqual(self.request(raw=b"not JSON")[0], 400)
        self.assertEqual(self.request(raw=b"null")[0], 400)
        self.assertEqual(self.request(raw=b"x" * 10001)[0], 400)
        self.assertEqual(self.request(raw=b"{}", content_type="text/plain")[0], 415)
        self.assertEqual(self.request("/api/missing")[0], 404)

    def test_lesson_assets_load_and_database_is_not_served(self):
        for path in example.STATIC:
            self.assertEqual(self.request(path)[0], 200, path)
        for path in ("/", "/task-manager/starter/", "/task-manager/solution/", "/activity-tracker/"):
            self.assertEqual(self.request(path)[0], 200, path)
        for path in ("/activities.sqlite3", "/serve.py", "/../data/activities.json"):
            self.assertEqual(self.request(path)[0], 404, path)


class LearnerDownload(unittest.TestCase):
    def test_archive_contains_current_examples_without_runtime_state(self):
        with ZipFile(packaging.ARCHIVE) as archive:
            files = list(packaging.example_files())
            expected = {"vibe-coding-examples/" + p.relative_to(ROOT).as_posix() for p in files}
            self.assertEqual(set(archive.namelist()), expected)
            for path in files:
                name = "vibe-coding-examples/" + path.relative_to(ROOT).as_posix()
                self.assertEqual(archive.read(name), path.read_bytes(), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
