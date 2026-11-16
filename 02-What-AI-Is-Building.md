---
title: "Understanding What AI Is Building"
teaching: 65
exercises: 85
---

:::::::::::::::::::::::::::::::::::::::: questions

- Where should I look when an AI generates a collection of code files?
- How can I follow an input through a function and predict the result?
- How can I investigate a problem and verify an AI-assisted change?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

- Locate the code responsible for one behaviour in a small application.
- Trace arguments, parameters, conditions, return values, and changes to state.
- Distinguish local imports, third-party packages, built-in capabilities, and configuration.
- Recognise an object, a method call, and a simple class definition.
- Use observed behaviour and error messages to request and verify a focused change.

::::::::::::::::::::::::::::::::::::::::

## From describing behaviour to inspecting code

In [Topic 1](01-ideas-to-computational-problems.md), we described a task manager
using pseudocode. Now imagine the AI has returned several files. How can we check
whether they implement our description?

Our goal is to connect **a requirement, the code responsible for it, and evidence
of its behaviour**. You do not need to memorise JavaScript syntax to make these
connections. We use JavaScript because the earlier example already runs in a
browser; the same questions apply to other languages.

Open the task-manager **starter** using the [setup instructions](../learners/setup.md).
The supplied files are a repeatable example of what an AI might generate.
You may inspect your own generated version later, but use the supplied version
for the shared exercises. It contains one deliberate validation bug.

| Block | Explanation and demonstration | Exercises | Total |
| --- | ---: | ---: | ---: |
| Orient yourself | 15 min | 15 min | 30 min |
| Follow one operation | 20 min | 25 min | 45 min |
| Reused code and settings | 15 min | 20 min | 35 min |
| Investigate and verify | 15 min | 25 min | 40 min |

Take a break after the second block. Break time is additional to these estimates.

## 1. Orient yourself: what are these files?

**Source code** is the human-readable instructions used to build or run software.
A **script** is a file containing instructions executed by a language runtime,
such as the browser's JavaScript engine or Python. Some software must first be
translated or built before it runs.

Our task-manager example has these responsibilities:

| File | Responsibility | A question it helps answer |
| --- | --- | --- |
| `starter/index.html` | Page structure, labels, inputs, and buttons | Where is the task-description input? |
| `style.css` | Presentation | Why do buttons look this way? |
| `starter/app.js` | Validate, add, display, complete, and delete tasks | Why was this description accepted? |
| `storage.js` | Load and save tasks in this browser | Why are tasks present after refreshing? |

For now, use filenames to identify responsibilities. We will explore directories
and paths more systematically in [Topic 3](03-Data-File-StructuredInfo.md).

A file can contain **comments**: notes for people reading the code. In JavaScript,
`//` begins a one-line comment. Comments and AI explanations are useful clues;
we still check the instructions that actually run.

:::::::::::::::::::::::::::::::::::::::: challenge

### First look: state your expectations (5 minutes)

Before opening the code, write the expected result of:

1. Adding `Read paper`.
2. Adding an empty description.
3. Adding a description containing only three spaces.

Use Topic 1's requirement: reject empty or whitespace-only descriptions. Do not
run the cases yet. Keep your predictions for the next block.

:::::::::::::::::::::::::::::::::::::::: solution

1. One new task should appear.
2. No task should be added; a helpful message should appear.
3. No task should be added; a helpful message should appear.

These are requirements, not claims about the starter's actual behaviour.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

### Start with a behaviour, then find its route

The HTML loads `app.js` using a script element. In `app.js`, some instructions
run when the module loads, while **event handlers** run in response to actions.
A function definition names a job; defining the function does not itself do that job.

```javascript
form.addEventListener("submit", (event) => {
  event.preventDefault();
  addTask(input.value);
});
```

Read this as: "When the form is submitted, prevent its default page navigation,
read the input value, and call `addTask` with that value."
The arrow `=>` introduces a function here. You only need to recognise its role.

The route we will inspect is:

```text
Submit the form
    -> read input.value
    -> addTask(description)
    -> validateTask(description)
    -> save and display, OR show a message
```

:::::::::::::::::::::::::::::::::::::::: challenge

### Map a behaviour to the code (10 minutes)

Open `starter/app.js` in an editor. Find:

1. The function that decides whether a description is accepted.
2. The instruction that saves the task list.
3. The function that updates the displayed list.
4. The event handler that connects the form to adding a task.

Compare your findings with a partner. Name a function you would inspect first
if tasks saved correctly but did not appear on screen.

:::::::::::::::::::::::::::::::::::::::: solution

1. `validateTask`.
2. `saveTasks(tasks)`.
3. `displayTasks`.
4. The `form.addEventListener("submit", ...)` block.

Start with `displayTasks` for a display problem, while remaining open to evidence
that an earlier operation supplied the wrong information.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

## 2. Follow one operation

### Parameters, arguments, and return values

```javascript
function validateTask(description) {
  return description.length > 0;
}

validateTask("Read paper");
```

- `description` is a **parameter**: a name for information the function receives.
- `"Read paper"` is an **argument**: the actual value supplied by this call.
- `.length` gives the number of characters in this string, including spaces.
- `>` compares values. Here, the comparison produces `true` or `false`.
- `return` sends a value back to the caller and ends that function call.

Returning a value does not automatically display or save it. The caller decides
what to do with the value. A function can also change something outside itself,
such as a displayed message or saved data; this is often called a **side effect**.

:::::::::::::::::::::::::::::::::::::::: challenge

### Trace the validator (10 minutes)

Complete this table without running the code. Represent three spaces as `"   "`.

| Argument | Value of `description.length` | Returned value | Matches requirement? |
| --- | --- | --- | --- |
| `"Read paper"` | | | |
| `""` | | | |
| `"   "` | | | |

Where do the behaviour of the code and the requirement diverge?

:::::::::::::::::::::::::::::::::::::::: solution

| Argument | Length | Return | Matches requirement? |
| --- | ---: | --- | --- |
| `"Read paper"` | 10 | `true` | Yes |
| `""` | 0 | `false` | Yes |
| `"   "` | 3 | `true` | No |

Spaces count as characters. The starter checks length, not meaningful content.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

### Conditions, early returns, and state

The beginning of `addTask` reads:

```javascript
function addTask(description) {
  if (!validateTask(description)) {
    message.textContent = "Please enter a task.";
    return;
  }
  // The remaining instructions create, save, and display the task.
}
```

`!` means "not". If validation returns `false`, the condition is true and we
enter the block. The bare `return;` ends `addTask` without a useful return value.
It prevents the later saving instructions from running.

When validation succeeds, `tasks.push(task)` adds an item to the in-memory list.
`saveTasks(tasks)` writes a stored representation. `displayTasks()` rebuilds the
visible list using a loop. **Changing state, saving it, and displaying it are
separate operations.**

:::::::::::::::::::::::::::::::::::::::: challenge

### Return or display? (5 minutes)

A learner says: "`validateTask` returns `false`, so the user sees `false`."
Explain what actually happens when `addTask("")` runs. Which function ends at
each `return`? Does `saveTasks` run?

:::::::::::::::::::::::::::::::::::::::: solution

The `return false` ends the call to `validateTask`. The caller uses that value
in its condition. `addTask` changes the visible message to "Please enter a task."
and its bare `return` ends `addTask`. `saveTasks` does not run for this input.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

### Compare prediction with observation (10 minutes)

In the starter, click **Clear practice tasks**. Try the three inputs from your
prediction table. Record the visible message and number of tasks after each case.
Spaces may produce a task with no visible description; count the task rows or
their Delete buttons. Delete this practice row afterwards.

For a normal task, also try Complete and refresh the page. Separate the evidence
that the display changed from the evidence that the completion status was saved.

Use the [observation worksheet](../learners/worksheet.md) if useful.

:::::::::::::::::::::::::::::::::::::::: solution

The normal description adds a task. The empty description produces a message
without adding a task. Three spaces incorrectly add a task. Completing changes
the display; seeing the completed status after refresh is evidence of saving and
reloading in this browser. It does not establish sharing with another browser.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

## 3. Recognise reused code and settings

### Imports are clues about dependencies

At the beginning of the supplied `app.js`:

```javascript
import { loadTasks, saveTasks } from "../storage.js";
```

This imports functions from another **local module**. A module groups code that
can be reused elsewhere. A **library** provides reusable capabilities; a
**package** is a distributable unit of code and associated information. A
third-party package may supply a library, but this example needs no installed
JavaScript packages.

`localStorage`, `JSON`, and browser page operations are built-in browser
capabilities. They do not need a package installation. A different project
might import third-party code and list required packages in a file such as
`package.json`. Ask which runtime and dependencies the project needs before
following generated installation instructions.

The word **dependency** has two related uses: Topic 1 described steps that depend
on earlier steps; here we also mean software that other code requires.

:::::::::::::::::::::::::::::::::::::::: challenge

### Sort the responsibilities (10 minutes)

Match each item to application code, local imported code, built-in capability,
or third-party package. Identify which item is absent from our task manager.

1. `validateTask` in `app.js`.
2. `saveTasks` supplied by `storage.js`.
3. `JSON.stringify` and `localStorage.setItem`.
4. A separately installed charting library used by a different dashboard.

If an AI says "the import failed", what information would you request before
asking it to rewrite the application?

:::::::::::::::::::::::::::::::::::::::: solution

1. Application code. 2. Local imported code. 3. Built-in capabilities.
4. Third-party package; absent from our example.

Ask for the exact error, import statement, module location or package name, and
the way the app was launched. A local import failure is not proof that an
additional package needs installing. For example, opening this app as a local
`file://` page instead of through the supplied server can prevent module loading.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

### Objects, properties, methods, and classes: recognition

```javascript
const task = { description: "Read paper", completed: false };
task.completed = true;
```

An **object** can group named values. Here `description` and `completed` are
**properties**. A function accessed through an object is called a **method**;
for example, `tasks.push(task)` calls the array's `push` method.

A **class** describes a way to create objects with related data and behaviour:

```javascript
// Recognition example only: the supplied task manager does not need a class.
class Task {
  constructor(description) {
    this.description = description;
    this.completed = false;
  }
  complete() {
    this.completed = true;
  }
}
const reading = new Task("Read paper");
reading.complete();
```

`reading` is an **instance** of `Task`. You do not need to design classes here.
Both examples represent a task, and objects can exist without a class we define.

:::::::::::::::::::::::::::::::::::::::: challenge

### Recognise the pieces (5 minutes)

In the class example, identify the class, instance, one property, and one method.
What is `reading.completed` after the last line? Does the snippet save anything
to persistent storage?

:::::::::::::::::::::::::::::::::::::::: solution

Class: `Task`; instance: `reading`; property: `description` or `completed`;
method: `complete`. The final completed value is `true`. There is no storage
operation, so this change alone does not establish persistence.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

### Configuration and environment variables

**Configuration** changes settings without rewriting the main behaviour.
An **environment variable** is a named setting passed to a running process by
its surrounding environment. It is different from a variable inside a function.

In Topic 4's Python server, `ACTIVITY_DB` can select the database file. Without
that setting, the server uses its documented default. A code example might read:

```python
database = os.environ.get("ACTIVITY_DB", "activities.sqlite3")
```

You only need to read this as "use the environment setting if present; otherwise
use this filename." The actual server also resolves the default location.
Environment changes normally affect a process when it starts, so restart it
after changing its settings.

Some settings hold credentials. Putting a secret in browser-delivered code or
in a browser build setting makes it available to the browser's user. Calling a
value an environment variable does not automatically keep it private.

:::::::::::::::::::::::::::::::::::::::: challenge

### Which setting belongs where? (5 minutes)

For each requirement, identify whether you would inspect application logic,
presentation, or configuration:

1. Reject descriptions containing only spaces.
2. Change button spacing.
3. Store the server's practice database in a different file.

Would a real private service key belong in a JavaScript file downloaded by users?

:::::::::::::::::::::::::::::::::::::::: solution

1. Validation logic. 2. CSS presentation. 3. Server configuration, such as
`ACTIVITY_DB`. A private key must not be delivered to the browser; a server can
hold it and expose only the operations users are allowed to request.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

## 4. Investigate a problem and verify a change

### Different failures need different evidence

| Situation | Example | Useful evidence |
| --- | --- | --- |
| Syntax error: code cannot be parsed | A missing closing quote | File, line, and parser message |
| Runtime error or exception: an operation fails while running | Reading `.length` from `null` | Error type, message, relevant call, and input |
| Behaviour differs from the requirement | Spaces become a saved task | Expected result, actual result, reproducible input |

An **exception** interrupts normal execution unless handled. A **stack trace**
shows a chain of calls associated with an error. Start with the error message
and the first relevant location in your own code. Exact wording varies between
browsers and versions.

Invalid user input can instead be an anticipated outcome: our empty-description
message is deliberate validation, not a thrown exception. Likewise, a program
can finish without an exception and still produce the wrong result.

:::::::::::::::::::::::::::::::::::::::: challenge

### Read the evidence (8 minutes)

These are separate prepared examples, not all failures in the starter:

```text
A. SyntaxError: Invalid or unexpected token
   app.js:12

B. TypeError: Cannot read properties of null (reading 'length')
   at validateTask (app.js:10)
   at addTask (app.js:14)

C. Expected: no task added for "   "
   Observed: task count increased from 1 to 2; no console error
```

Classify each failure. For B, which value would you investigate first? Would
removing validation entirely resolve the requirement demonstrated by C?

:::::::::::::::::::::::::::::::::::::::: solution

A: syntax error. B: runtime exception; investigate how `null` reached the
description parameter. C: incorrect behaviour. Removing validation might hide
symptoms but would allow more invalid tasks; it would not satisfy the requirement.
Line numbers here illustrate how to locate evidence, not the current source layout.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

### Request a focused change

Prefer an evidence-based request over "fix the app":

> In the task-manager starter, `validateTask` rejects an empty string but accepts
> three spaces. Both should be rejected. Change the validator to reject empty or
> whitespace-only descriptions. Keep adding, completing, deleting, and saving
> tasks working. Explain the cause, show the changed lines, and give checks for
> a normal description, an empty string, and spaces only. Avoid extra features.

An AI explanation is a proposal to check. Review the changed lines and run the
cases yourself. If the response replaces many unrelated files, ask why the
change needs that scope before accepting it.

:::::::::::::::::::::::::::::::::::::::: challenge

### Repair and verify (12 minutes)

1. Keep a copy of the starter or use the supplied solution as a comparison.
2. Ask an AI assistant for the targeted change above. Without an assistant,
   propose the change in plain language, then reveal the solution.
3. Inspect the changed lines. Do they implement the stated rule?
4. Repeat the three validation cases. Also complete and delete a normal task,
   and refresh to check saving.
5. Record one observation that could disprove the claim "the repair works".

If editing the supplied files, reload the page to load the edited JavaScript.
The starter and solution have separate practice lists.

:::::::::::::::::::::::::::::::::::::::: solution

One focused repair is:

```javascript
function validateTask(description) {
  return description.trim().length > 0;
}
```

`trim()` returns a string without surrounding whitespace. It does not change
the original description. A normal description is accepted; empty and
whitespace-only strings are rejected. The [solution source](files/task-manager/solution/app.js)
contains this repair. Check the browser app using the solution URL in setup.

Adding a whitespace-only task after repair would disprove the claim. Failure
to complete, delete, or reload a valid task would show another behaviour changed.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

### Exit ticket: transfer the reasoning (5 minutes)

This independent example checks hours worked:

```javascript
function validHours(hours) {
  return hours > 0 && hours <= 24;
}
```

`&&` means "and". Identify the parameter and possible returned values. Predict
the results for `0`, `2.5`, and `25`. Name one boundary case to check. Does this
function save or display anything? Explain without asking an AI assistant.

:::::::::::::::::::::::::::::::::::::::: solution

Parameter: `hours`. Return: a Boolean (`true` or `false`). Results: `false`,
`true`, `false`. Useful boundary cases include `24` (accepted) and a value just
above `24` (rejected). This function neither saves nor displays data. A complete
validator would also need agreed rules about types and missing values.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: instructor

### Delivery notes

Use the four timing blocks above; challenge times include discussion and feedback.
Keep each explanation short and let learners predict before running code.
Give quiet thinking time before pair comparison; learners can also work alone.
The reading snippets are selected portions, not instructions to type a whole app.

Before class, test the starter and solution through the supplied server. Both
normal and private-browser storage must be checked for the browsers you teach.
If storage is disabled or contains malformed data, use a fresh browser profile
or the prepared observation evidence rather than spending the lesson on repair.

Misconceptions to revisit: defining a function calls it; returning displays;
an import always means installing a package; an object requires a custom class;
no exception means correct output; an AI explanation proves a change works.

The classes example is recognition only. Package-management commands and class
design are optional extensions. The core repair can be completed without an AI
account by revealing the solution after a learner has explained the intended change.
See the shared [instructor notes](../instructors/instructor-notes.md).

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Connect a requirement to the responsible code and a behavioural check.
- A parameter names an input; an argument supplies it; a return value goes to the caller.
- Validation, state changes, persistent storage, and display are separate operations.
- Imports can refer to local code; built-in capabilities and third-party packages differ.
- Objects group properties and methods; classes are one way to create objects.
- Configuration changes settings; environment variables are supplied to a process.
- Errors and incorrect behaviour need evidence, a focused change, and independent checks.

::::::::::::::::::::::::::::::::::::::::

## Further reading

- [MDN: JavaScript functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions).
- [MDN: JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).
