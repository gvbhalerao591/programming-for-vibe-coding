---
title: Setup
---

## What you need

This course assumes little or no programming experience. Before the workshop,
check that you can open a folder, edit a plain-text file, and use a web browser.
Ask the teaching team for help with setup before the first session if possible.

- A laptop with a recent Firefox, Chrome, Edge, or Safari browser.
- A plain-text/code editor that preserves file extensions and indentation.
- Python 3.9 or newer with its standard `sqlite3` module, for the local examples.
  No additional Python or JavaScript packages are required for these examples.
- The course files, downloaded before the workshop.
- Access to the AI coding assistant selected by the organisers, if available.
  Organisers should communicate account arrangements in advance. Prepared code
  and solutions support participation without an AI account.

R, RStudio, Git, Node.js, a database application, and a public hosting account
are not required for learners. R and Workbench are lesson-authoring tools.

## Get the files

Download the [teaching examples ZIP](../episodes/data/vibe-coding-examples.zip)
and extract it. Open the extracted `vibe-coding-examples` folder. If your archive
tool adds an outer folder, open the inner folder that contains `episodes`.
Keep the folder structure intact: code and example data refer to each other.

Alternatively, download or clone the
[full repository](https://github.com/gvbhalerao591/programming-for-vibe-coding).
In either case, work from the folder containing `episodes/files/serve.py`.
You do not need to learn Git for this workshop.

The data are synthetic research activities. The supplied
[CSV](../episodes/data/activities.csv) and [JSON](../episodes/data/activities.json)
contain the same three records as Topic 3. Practice with these rather than
personal or confidential records.

## Start the local examples

These commands start one program that serves both examples on your laptop.
They are setup steps: understanding terminal syntax is not a prerequisite.
An instructor can help or run a demonstration you can follow.

:::::::::::::::::::::::::::::::::::::::: spoiler

### Windows

Install Python 3 from [python.org](https://www.python.org/downloads/) if needed.
Open the extracted course folder in File Explorer, then open a terminal there
(for example, right-click and choose **Open in Terminal**). In PowerShell run:

```powershell
py -3 --version
py -3 -c "import sqlite3; print('SQLite ready')"
py -3 episodes/files/serve.py
```

If `py` is unavailable but `python --version` reports Python 3.9 or newer, use
`python` in place of `py -3`. Ask a helper if neither works.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: spoiler

### macOS

Install Python 3 from [python.org](https://www.python.org/downloads/) if needed.
Open Terminal. Type `cd ` (including the space), drag the extracted course
folder into Terminal to insert its path, then press Return. Run:

```bash
python3 --version
python3 -c "import sqlite3; print('SQLite ready')"
python3 episodes/files/serve.py
```

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: spoiler

### Linux

Open a terminal in the extracted course folder using your file manager, or use
`cd` to enter it. Run:

```bash
python3 --version
python3 -c "import sqlite3; print('SQLite ready')"
python3 episodes/files/serve.py
```

If Python or `sqlite3` is missing, use your distribution's documented installation
method or ask local IT. Organisers can provide a prepared machine or demonstration
where installation is restricted.

::::::::::::::::::::::::::::::::::::::::

Leave the terminal open. Copy the appropriate URL into your browser address bar:

| Example | Browser address |
| --- | --- |
| Task manager: starter | `http://127.0.0.1:8000/task-manager/starter/` |
| Task manager: solution | `http://127.0.0.1:8000/task-manager/solution/` |
| Research activity tracker | `http://127.0.0.1:8000/activity-tracker/` |

Use the starter until invited to inspect the solution. Do not open the HTML files
by double-clicking: module imports and API requests need the local server.
Here, local means the browser and server run on your laptop.

Stop with Ctrl+C in the terminal. Start again with the same command. The activity
database is kept at `episodes/files/activities.sqlite3`. To reset to the three seed
activities, stop the server, **rename** that file to a backup name, then restart.
Browser tasks are separate: use **Clear practice tasks** in the appropriate
version to clear its practice list.

## Before-class readiness check

1. Open the starter. Add `Setup check`, complete it, and refresh. Confirm that
   it is still complete. Then delete it. This checks browser storage is available.
2. Open the activity tracker. Confirm three seed activities on a fresh database.
   Add `Setup check` with `0.5` hours and refresh. Confirm it remains. More than
   three records is normal if you have already practised.
3. Open `episodes/files/task-manager/starter/app.js` in your editor and find
   `validateTask`; do not repair it yet.
4. Find developer tools in your browser menu, then the Network panel. Menu names
   vary; a helper can guide this during the workshop.

After downloading, the local examples work without internet. An online AI
assistant may still need connectivity. Without a runnable example, use the
[worksheet](worksheet.md) and
[request transcripts](request-transcripts.md) with an instructor
or partner. Their reasoning tasks cover the same concepts.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| Python cannot find `episodes/files/serve.py` | Work from the folder containing `episodes`; check for an extra outer ZIP folder. |
| Address already in use | Add `--port 8001` after `serve.py`, then use port 8001 in every example URL. |
| Browser cannot connect | Confirm the server is running; check the printed address and port. |
| Page loads but controls do nothing | Use the HTTP URL, not `file://`; show the browser console error to a helper. |
| Task storage unavailable | Try a permitted browser/profile or use prepared observations if policy blocks storage. |
| Different task list at `localhost` | Return to `127.0.0.1` and the original port; storage depends on the origin. |
| Activities differ after restart | Check the database path printed at startup. |

The server listens only at `127.0.0.1`. A colleague opening that address on their
laptop reaches their own computer, not yours.
