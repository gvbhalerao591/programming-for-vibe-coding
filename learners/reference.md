---
title: Reference
---

## Read and verify generated code

1. State required behaviour and a concrete input/output example.
2. Find where input enters and which function handles it.
3. Follow arguments into parameters and conditions; identify return values.
4. Separate changes to memory, storage, and the visible result.
5. Check imports and configuration before assuming a missing dependency.
6. Record expected and observed behaviour, including invalid input.
7. Request a focused change; inspect changed lines and repeat checks.

Useful request pattern:

> For this input, I expected X and observed Y. Here is the relevant code/error.
> Explain the cause and propose a focused change. Show changed lines and checks
> for normal, invalid, and boundary inputs. Keep these existing behaviours working.

## Investigate a web application

Follow evidence through:

```text
Browser action -> request -> server checks -> storage operation
    -> response -> optional retrieval request -> displayed result
```

Record method, URL, payload, response status/body, and visible behaviour. A
record in a GET response but absent on screen suggests a different investigation
from a rejected save request.

## Specify an application

Name users, inputs, validation rules, outputs, state, persistent storage, access
rules, and failure behaviour. Say who hosts and maintains a shared app. Write
acceptance checks before asking an AI to implement it.

## Glossary

| Term | Meaning in this course |
| --- | --- |
| Acceptance check | A concrete observation used to assess a requirement. |
| API | An agreed interface through which software requests operations. |
| Argument | An actual value supplied when calling a function. |
| Authentication | Establishing who a user is. |
| Authorisation | Deciding what an identified user is allowed to do. |
| Back end | Application work carried out on a server. |
| Boolean | A true/false value, different from text such as `"false"`. |
| Browser | Client software that loads pages and can execute JavaScript. |
| Class | A definition used to create objects with related data and behaviour. |
| Client | Software that requests something from a server. |
| Configuration | Settings that influence how software runs. |
| Database | Organised stored data and facilities for retrieving/changing it. |
| Dependency | A required preceding step, or software required by other software. |
| Deployment | Placing software and settings into a running environment. |
| Domain | A human-readable name that can resolve to a network address. |
| Environment variable | A named setting supplied to a process by its environment. |
| Exception | A runtime event interrupting normal execution unless handled. |
| Field | A named attribute of a record. |
| Front end | The user-facing part, here running in the browser. |
| Function | A named operation that may accept inputs and return a result. |
| Hosting | Resources/services used to run and serve an application. |
| HTTP / HTTPS | A request/response protocol / its protected transport form. |
| Import | A statement making code from another module available. |
| Instance | An object created from a class. |
| Library | Reusable code providing capabilities to other code. |
| localStorage | Browser storage associated with an origin and browser profile. |
| Loopback / localhost | An address / name referring back to this computer. |
| Method | A function associated with an object; in HTTP, an operation such as GET. |
| Module | A unit of code that can expose parts for other code to use. |
| Object | A value grouping properties and possibly methods; usage varies by language. |
| Origin | A URL's scheme, host, and port, used in browser storage/security rules. |
| Package | A distributable unit of code and associated information. |
| Parameter | A name for input received by a function. |
| Persistence | Keeping information beyond an operation or process lifetime. |
| Property | A named value associated with an object. |
| Record | Information about one item or observation. |
| Return value | A value sent back from a function to its caller. |
| Route | A mapping from a request method and path to server behaviour. |
| Runtime | Software that executes a program's instructions. |
| Script | A file of instructions executed by a language runtime. |
| Server | Software responding to requests; also the computer running it. |
| Side effect | A change outside a returned value, such as saving data. |
| Source code | Human-readable instructions used to build or run software. |
| Stack trace | A chain of calls reported with an error. |
| State | Information representing a program's current situation. |
| Validation | Checking information against agreed rules. |

## Practice resources

- [Setup and readiness check](setup.md).
- [Printable worksheet](worksheet.md).
- [Prepared request evidence](request-transcripts.md).
- [Downloadable examples](../episodes/data/vibe-coding-examples.zip).
