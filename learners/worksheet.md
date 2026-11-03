---
title: Observation Worksheet
---

Work individually first, then compare with a partner. An instructor can print
this worksheet or learners can copy the tables into their own notes.

## Topic 2: task-manager validation

Requirement: accept meaningful descriptions; reject empty and whitespace-only
descriptions. Start by clearing practice tasks. Record counts before and after
each input, including rejected inputs.

| Input | Expected behaviour | Observed message and task counts | Matches? |
| --- | --- | --- | --- |
| `Read paper` | | | |
| Empty string | | | |
| Three spaces | | | |

Responsible function:

Cause proposed from code:

Requested change:

Changed lines reviewed:

| Check after repair | Observation | Evidence still needed |
| --- | --- | --- |
| Normal description | | |
| Empty description | | |
| Spaces only | | |
| Complete a normal task | | |
| Refresh after completion | | |
| Delete and refresh | | |

## Topic 4: request and response

| Action | Method and URL | Request data | Status and response | Visible result |
| --- | --- | --- | --- | --- |
| Load activities | | | | |
| Save a valid activity | | | | |
| Submit spaces-only activity | | | | |
| Reload while server is stopped | | | | |

## Topic 4: persistence

Use the same URL and port for each check. For "different browser", use a
separate browser or profile on the same laptop, with the same local server.

| Experiment | Prediction for browser tasks | Observation | Prediction for server activities | Observation |
| --- | --- | --- | --- | --- |
| Refresh | | | | |
| Different browser/profile | | | | |
| Restart server with same database | | | | |

What does the evidence support?

What has not been established (for example, access from a colleague's laptop)?

## Final specification

Users and intended access:

Inputs and validation rules:

What runs in the browser:

What the server checks and does:

Where data persists:

What a successful save response means:

What the user should see if saving fails:

Three acceptance checks, including one failure case:
