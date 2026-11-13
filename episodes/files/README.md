# Local teaching examples

From the folder containing `episodes`, run:

```bash
python3 episodes/files/serve.py
```

On Windows use `py -3` instead of `python3`. Python 3.9+ with SQLite is sufficient;
no extra packages, Node.js, or public services are needed. Open:

- Starter: `http://127.0.0.1:8000/task-manager/starter/`
- Solution: `http://127.0.0.1:8000/task-manager/solution/`
- Activities: `http://127.0.0.1:8000/activity-tracker/`

The starter intentionally accepts whitespace-only task descriptions. The solution
repairs that validator. Both save lists in browser localStorage with separate
keys per version. Clear practice tasks clears only that version's list. Source
files need the server; do not launch HTML using `file://`.

The activity tracker seeds three synthetic records from
`episodes/data/activities.json` on a fresh database. Subsequent records are stored
in `episodes/files/activities.sqlite3` and survive restarts. Stop with Ctrl+C.
To reset, stop the server, rename the database to a backup name, then restart.
Use `--port 8001` if 8000 is occupied. `ACTIVITY_DB` can select another database
file; its parent directory must exist.

The API supports GET and POST `/api/activities`. POST requires JSON with
`activity` (nonblank string) and `hours` (number greater than 0 and at most 24).
The server trims activity, assigns its ID, sets completion to false, and commits
before returning 201. Invalid submissions return 400 without insertion. No login
or role enforcement is implemented. This loopback teaching server is not a
production hosting recipe.

Setup and lesson pages explain the exercises. Offline alternatives are in
`learners/worksheet.md` and `learners/request-transcripts.md`.
