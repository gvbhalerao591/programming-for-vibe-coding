"""Rebuild the learner download deterministically from the checked-in examples."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "episodes/data/vibe-coding-examples.zip"


def example_files():
    for directory in (ROOT / "episodes/files", ROOT / "episodes/data"):
        for path in sorted(directory.rglob("*")):
            if (path.is_file() and "__pycache__" not in path.parts
                    and path.suffix in {".py", ".js", ".css", ".html", ".md", ".csv", ".json"}):
                yield path
    yield ROOT / "learners/worksheet.md"
    yield ROOT / "learners/request-transcripts.md"


def main():
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED) as archive:
        for path in example_files():
            name = "vibe-coding-examples/" + path.relative_to(ROOT).as_posix()
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"Built {ARCHIVE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
