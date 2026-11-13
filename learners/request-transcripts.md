---
title: Prepared Request Evidence
---

Use these text equivalents when the live example or browser developer tools
are unavailable. Headers unrelated to the exercise are omitted. These are
illustrations of the supplied app; actual IDs depend on earlier additions.

## A. Retrieve, save, and retrieve again

Request:

```http
GET /api/activities HTTP/1.1
```

Response:

```http
HTTP/1.0 200 OK
Content-Type: application/json; charset=utf-8

[
  {"id":101,"activity":"Literature review","hours":2.5,"completed":true},
  {"id":102,"activity":"Clean survey data","hours":1.0,"completed":false},
  {"id":103,"activity":"Draft report","hours":3.0,"completed":false}
]
```

Request after submitting a valid form:

```http
POST /api/activities HTTP/1.1
Content-Type: application/json

{"activity":"Read methods","hours":1.5}
```

Response:

```http
HTTP/1.0 201 Created
Content-Type: application/json; charset=utf-8

{"id":104,"activity":"Read methods","hours":1.5,"completed":false}
```

Visible message: `Activity 104 saved.`

The browser then sends another `GET /api/activities`. It receives status 200
and an array of four records, including ID 104. After the browser redraws the
list, `Read methods: 1.5 hours` appears.

## B. Reject whitespace-only text

Request:

```http
POST /api/activities HTTP/1.1
Content-Type: application/json

{"activity":"   ","hours":1}
```

Response:

```http
HTTP/1.0 400 Bad Request
Content-Type: application/json; charset=utf-8

{"error":"Enter an activity description."}
```

Visible message: `Request failed: Enter an activity description.`
No activity is added. Input remains in the form. A later GET returns the same
records as before this rejected request.

## C. Connection failure

The server has been stopped. The browser attempts `GET /api/activities` after
the user clicks Reload list. No HTTP response arrives. Developer tools show a
connection failure rather than a 400 or 500 response. The page reports a failed
request; exact browser wording varies. Restarting the same server and clicking
Reload list retrieves the saved records again.

## D. A display fault: reasoning scenario only

This fault is not intentionally included in the runnable activity tracker.
Suppose POST returns 201 and a subsequent GET includes ID 104, but the display
still lists only IDs 101 to 103. The evidence supports inspecting rendering
and the way retrieved data reaches it. It does not support assuming the save
failed or replacing the database.

## E. Access control: proposed future feature

The runnable tracker has no accounts. In a future role-based version, a signed-in
viewer attempts to add a record. The server denies permission and creates no
record. This requires an identity mechanism and a server permission check;
it cannot be demonstrated as an existing feature of this example.
