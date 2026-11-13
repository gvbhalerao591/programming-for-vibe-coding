"""Local teaching examples. Run from any directory; no third-party packages needed."""

import argparse
import json
import math
import os
from pathlib import Path
import sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
SEED = ROOT.parent / "data" / "activities.json"
STATIC = {
    "/task-manager/style.css": "text/css",
    "/task-manager/storage.js": "text/javascript",
    "/task-manager/starter/index.html": "text/html",
    "/task-manager/starter/app.js": "text/javascript",
    "/task-manager/solution/index.html": "text/html",
    "/task-manager/solution/app.js": "text/javascript",
    "/activity-tracker/index.html": "text/html",
    "/activity-tracker/app.js": "text/javascript",
}


def initialise_database(database):
    # Seed once. Restarting must not replace learners' saved records.
    with closing(sqlite3.connect(database)) as connection, connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS activities "
            "(id INTEGER PRIMARY KEY, activity TEXT, hours REAL, completed INTEGER)"
        )
        if not connection.execute("SELECT COUNT(*) FROM activities").fetchone()[0]:
            for record in json.loads(SEED.read_text(encoding="utf-8")):
                connection.execute(
                    "INSERT INTO activities VALUES (?, ?, ?, ?)",
                    (record["id"], record["activity"], record["hours"], record["completed"]),
                )


class CourseHandler(BaseHTTPRequestHandler):
    def reply(self, status, body, content_type="application/json"):
        if content_type == "application/json":
            body = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/":
            self.reply(200, b'<h1>Course examples</h1><ul>'
                       b'<li><a href="/task-manager/starter/">Task manager: starter</a></li>'
                       b'<li><a href="/task-manager/solution/">Task manager: solution</a></li>'
                       b'<li><a href="/activity-tracker/">Activity tracker</a></li></ul>',
                       "text/html")
        elif path == "/api/activities":
            with closing(sqlite3.connect(self.server.database)) as connection:
                rows = connection.execute(
                    "SELECT id, activity, hours, completed FROM activities ORDER BY id"
                ).fetchall()
            records = [dict(id=r[0], activity=r[1], hours=r[2], completed=bool(r[3]))
                       for r in rows]
            self.reply(200, records)
        else:
            if path.endswith("/"):
                path += "index.html"
            if path in STATIC:
                self.reply(200, (ROOT / path.lstrip("/")).read_bytes(), STATIC[path])
            else:
                self.reply(404, {"error": "No resource at this address."})

    def do_POST(self):
        if urlsplit(self.path).path != "/api/activities":
            self.reply(404, {"error": "No resource at this address."})
            return
        if self.headers.get_content_type() != "application/json":
            self.reply(415, {"error": "Send JSON with Content-Type: application/json."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 10000:
                raise ValueError("Request body must contain 1 to 10000 bytes.")
            record = json.loads(self.rfile.read(length))
            if not isinstance(record, dict):
                raise ValueError("Send one activity record as a JSON object.")
            activity = record.get("activity")
            hours = record.get("hours")
            if not isinstance(activity, str) or not activity.strip():
                raise ValueError("Enter an activity description.")
            if (type(hours) not in (int, float) or not math.isfinite(hours)
                    or not 0 < hours <= 24):
                raise ValueError("Hours must be a number greater than 0 and at most 24.")
        except (ValueError, OverflowError, UnicodeDecodeError) as error:
            self.reply(400, {"error": str(error)})
            return
        with closing(sqlite3.connect(self.server.database)) as connection, connection:
            cursor = connection.execute(
                "INSERT INTO activities (activity, hours, completed) VALUES (?, ?, ?)",
                (activity.strip(), hours, False),
            )
            result = dict(id=cursor.lastrowid, activity=activity.strip(),
                          hours=hours, completed=False)
        self.reply(201, result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    database = Path(os.environ.get("ACTIVITY_DB", ROOT / "activities.sqlite3"))
    initialise_database(database)
    with ThreadingHTTPServer(("127.0.0.1", args.port), CourseHandler) as server:
        server.database = database
        print(f"Open http://127.0.0.1:{server.server_port}/", flush=True)
        print(f"Activity database: {database.resolve()}", flush=True)
        print("Stop with Ctrl+C. Restarting keeps saved activities.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
