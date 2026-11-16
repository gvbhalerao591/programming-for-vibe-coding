---
title: Instructor Notes
---

## Status and intended audience

This is an initial teaching scaffold for a two-day course. Topics 1 and 3 are
existing contributions; Topics 2 and 4 extend them with prepared examples.
Timings are estimates to revise after a novice walkthrough and pilot delivery.
The intended learner has domain knowledge but little formal programming training.

The outcome is to specify, explain, investigate, and assess small AI-generated
programs. Learners are not expected to independently write a web back end, design
class hierarchies, implement authentication, or deploy a production service.

## Suggested two-day schedule

| Time | Day 1 | Day 2 |
| --- | --- | --- |
| 09:00–09:20 | Welcome, expectations, readiness check | Recap: inputs, behaviour, evidence |
| 09:20–10:20 | Topic 1: first half | Topic 3: first half |
| 10:20–10:35 | Break | Break |
| 10:35–11:35 | Topic 1: second half | Topic 3: second half |
| 11:35–12:00 | Guided practice and questions | Guided practice and questions |
| 12:00–12:45 | Lunch | Lunch |
| 12:45–14:00 | Topic 2: orientation and tracing | Topic 4: parts and requests |
| 14:00–14:15 | Break | Break |
| 14:15–15:30 | Topic 2: reuse, settings, investigation | Topic 4: storage, access, specification |
| 15:30–15:50 | Repair clinic or unfinished practice | Architecture/specification clinic |
| 15:50–16:00 | Reflection and feedback | Reflection and feedback |

Each new topic has 65 minutes of explanation/demonstration and 85 minutes of
exercises, including discussion and feedback. Practice periods are additional
support, not hidden requirements for core exercises. Topic 2's exit ticket is
within its 150 minutes; final reflection reviews the broader course.

## Preparation

1. Follow [learner setup](../learners/setup.md) from a fresh extracted ZIP on
   the operating systems used in the workshop. Check Python 3.9+, SQLite,
   browser module loading, and browser storage. No packages need installing.
2. Start `python3 episodes/files/serve.py` (Windows: replace `python3` with `py -3`).
   Keep it running for both examples. Check URLs, developer tools, and zoom.
3. Use a fresh database or rename the previous one while the server is stopped.
   Default: `episodes/files/activities.sqlite3`. Reset task lists with each version's
   Clear practice tasks button. Starter and solution store separately.
4. Complete both lessons' exercises yourself. Arrange a second browser/profile
   on the same laptop. Check restart persistence using the same database.
5. Provide the ZIP, worksheet, and request transcripts before class. Print or
   download evidence for restricted devices or connectivity failures.
6. Communicate AI account arrangements and the route without an account. Test
   any live generation beforehand.
7. Organise helpers and shared notes. Invite learners to signal when they need
   help without requiring a public explanation.

## Teaching approach

Introduce one small idea, model reading it, ask for a prediction, then run or
inspect it together. Allow quiet thinking before pair discussion. Offer individual
participation and rotate optional driver/navigator roles. Assess explanations
and evidence rather than speed or exact syntax. Expand terms on first use and
name the destination before switching windows.

The prepared starter rejects empty descriptions but accepts spaces. Let learners
predict and observe before revealing `.trim()`. The solution changes the validator
only. Comparing a newly AI-generated version belongs in the clinic, after the
common objectives are met.

In Topic 4 move between browser action, selected request, response, and visible
result. Keep `serve.py` implementation details in instructor discussion unless
asked. The goal is reasoning across boundaries.

## Formative checks

| Check | Evidence of intended understanding |
| --- | --- |
| Locate validation | Identifies `validateTask`, not CSS or storage code. |
| Trace spaces | Length is 3; starter returns true despite requirement. |
| Return versus display | Return reaches caller; `textContent` changes display. |
| Recognise import | `storage.js` is local; `JSON` is built in; no JS packages installed. |
| Recognise class | Distinguishes `Task`, `reading`, property, method. |
| Inspect GET/POST | Identifies method, path, payload, status, response. |
| Invalid activity | Spaces pass browser required check; server returns 400; no insertion. |
| Persistence | Tasks follow browser/profile and origin; activities follow server/database. |
| Save versus display | A GET can contain a record omitted by faulty rendering. |
| Access scenario | Requires server permission check; hiding a button is insufficient. |

Use the Topic 2 transfer question and Topic 4 specification as individual
assessment before discussion. Invite one concept that now makes sense and one
remaining question during reflection. Adjust explanations from those responses.

## Fallback delivery

| Constraint | Equivalent participation |
| --- | --- |
| No AI account/service | Describe intended change, then inspect prepared repair and repeat checks. |
| Python cannot run | Pair with working laptop or predict before projected demonstration. |
| Developer tools inaccessible | Annotate supplied request transcripts. |
| Only one browser/profile | Predict separate-browser results and compare prepared observations. |
| Storage restricted | Use permitted fresh profile or prepared observations. |
| Time pressure | Preserve prediction, repair, one request inspection, persistence reasoning, final specification. |

Class design, package installation, full login flows, SQL, and public deployment
are extensions. Class recognition remains a short core activity.

## Example design and boundaries

The task manager is browser-side code with a local storage helper module.
The server delivers assets but does not save tasks. Both versions support adding,
completing/reopening, deleting, refreshing, and clearing practice data.

The activity tracker uses Python's standard HTTP and SQLite libraries, serves
an explicit set of lesson assets, exposes GET/POST `/api/activities`, validates
on the server, and persists accepted records. New records have a server-assigned
ID and `completed: false`. The server binds only to loopback.

`ACTIVITY_DB` selects a database file for separate sessions. On macOS/Linux:

```bash
ACTIVITY_DB=/tmp/afternoon-activities.sqlite3 python3 episodes/files/serve.py --port 8001
```

In PowerShell, set it before starting:

```powershell
$env:ACTIVITY_DB = "$env:TEMP/afternoon-activities.sqlite3"
py -3 episodes/files/serve.py --port 8001
```

Use a new filename for fresh seed data. The parent directory must exist. Port
changes also change the browser storage origin.

This is a local teaching server, not a production deployment template. It has
no login, roles, update/delete API, or concurrency-conflict exercise. Role and
hosting scenarios are proposed requirements. The stale-display case is prepared
evidence, not an intentional bug in the runnable activity tracker.

## Author checks and maintenance

From the repository root, rebuild the archive after changing examples or data:

```bash
python3 scripts/package-examples.py
python3 scripts/check-examples.py
```

The check script uses temporary storage and an ephemeral loopback port; it does
not change practice records. A browser walkthrough is also needed to assess
interaction, accessibility, and teaching flow. With `sandpaper` installed, run:

```r
sandpaper::validate_lesson()
sandpaper::build_lesson()
```

Inspect episode order, downloads, figure descriptions, challenge/solution nesting,
learner/instructor views, and relative links in the rendered site. Do not edit
generated files under `site/`.

References: [Workbench episode structure](https://carpentries.github.io/sandpaper-docs/episodes.html),
[memory and cognitive load](https://carpentries.github.io/instructor-training/05-memory.html),
and [building skill with feedback](https://carpentries.github.io/instructor-training/06-feedback.html).
