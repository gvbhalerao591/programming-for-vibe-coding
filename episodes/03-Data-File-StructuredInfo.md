---
title: "Data, Files and Structured Information"
teaching: 85
exercises: 35
---

:::::::::::::::::::::::::::::::::::::::: questions

- How does software represent, store, and exchange information?
- How can I recognize a file format and describe its structure to an AI coding agent?
- How can I tell whether a conversion preserved the meaning of my data?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: objectives

- Navigate a simple project folder and interpret relative and absolute file paths.
- Distinguish file extensions, file formats, and the contents of a file.
- Recognize common data types and explain why they matter.
- Identify records and fields in tabular data.
- Read and compare CSV, TSV, JSON, and YAML representations.
- Describe a data-conversion workflow, including validation and verification.
- Write an actionable specification for an AI agent to transform data safely.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction: the same information, different representations

Imagine you are collecting a small list of research activities. You want to store it, inspect it in a spreadsheet, and eventually display it in a website. An AI coding agent offers to convert your data, but first you need to describe **what the information means** and **how it is organized**.

Throughout this episode, we will work with the same three records:

| id | activity | hours | completed |
| --- | --- | ---: | --- |
| 101 | Literature review | 2.5 | true |
| 102 | Clean survey data | 1.0 | false |
| 103 | Draft report | 3.0 | false |

The values are illustrative. We will ask how to store these records, move them between tools, and check that nothing important changes along the way.

::::::::::::::::::::::::::::::::::::::::: callout

### Why this matters for vibe coding

An AI agent can write code that opens a file or transforms data, but it may guess the wrong file path, treat an ID as a number, misread a delimiter, or silently drop information. Knowing the structure of your data helps you specify the task and verify the result.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 1. Files, directories, and paths

A **file** holds information. A **directory** (or folder) organizes files and other directories. A **path** tells a program where to find a file.

A small project might look like this:

```text
research-tracker/
├── README.md
├── data/
│   ├── activities.csv
│   └── activities.json
├── output/
└── scripts/
    └── convert.py
```

If we are working from inside `research-tracker/`, the **relative path** to the CSV file is:

```text
data/activities.csv
```

An **absolute path** starts at the root of a filesystem (or includes a drive on Windows), for example `/home/learner/research-tracker/data/activities.csv`. Absolute paths vary between computers. Relative paths are often more portable, but depend on the current working directory.

A filename extension such as `.csv` is a useful clue about a file's format; it does not guarantee that the contents are valid CSV.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Find the file (5 minutes)

Suppose the working directory is `research-tracker/`.

1. Write the relative path to `activities.json`.
2. Where would you save a newly generated `activities.tsv` without overwriting the source?
3. If your working directory changes to `scripts/`, what relative path reaches `activities.csv`?

:::::::::::::::::::::::::::::::::::::::: solution

1. `data/activities.json`
2. For example, `output/activities.tsv`.
3. `../data/activities.csv` — `..` means the parent directory.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## 2. Data types: what does a value mean?

Programs need to distinguish different kinds of values. Common **data types** include:

| Type | Example | Meaning |
| --- | --- | --- |
| Text / string | `"101"` | Characters; useful for IDs, names, and labels |
| Integer | `101` | Whole number |
| Decimal number | `2.5` | Numeric quantity |
| Boolean | `true` | True or false |
| Missing / null | `null` | No value is present |
| List / array | `["review", "write"]` | Ordered collection |
| Object / mapping | `{"hours": 2.5}` | Named fields with values |

Why care? The text `"101"` and the number `101` look similar, but behave differently. For example, identifiers such as `"00101"` should usually remain text so that leading zeros are preserved. The text `"false"` is not the same value as the Boolean `false`.

CSV and TSV store text fields; a program must decide whether a field represents a number, Boolean, date, or something else. JSON can represent several types directly. YAML also supports typed values, but automatic type interpretation can vary by parser and YAML version.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Choose a type (5 minutes)

Choose an appropriate type for each item and explain any ambiguity:

1. Participant ID `"0007"`
2. Number of responses `42`
3. Whether consent was recorded
4. A date written `2026-10-27`
5. An unknown age

:::::::::::::::::::::::::::::::::::::::: solution

1. String: preserve leading zeros.
2. Integer.
3. Boolean if only yes/no are possible; consider a separate missing/unknown state if needed.
4. Often a string in a standardized date format, or a date type in a system that supports one. JSON has no native date type.
5. Missing/null rather than `0`, since zero has a different meaning.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## 3. Tables, records, and fields

A **table** organizes information into rows and columns. A **record** is one observation or item (usually a row), and a **field** is one named attribute (usually a column).

For our example, the first record has `id = 101`, `activity = Literature review`, `hours = 2.5`, and `completed = true`.

A good table uses consistent field names and meaning. Decide whether every record must have an ID, whether duplicate IDs are allowed, and what a missing value means. These are **data rules** an AI agent should not invent.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Design a record (5 minutes)

You want to track reading materials. Propose four fields for each reading record. Which field would uniquely identify a record? What should happen when the publication year is unknown?

:::::::::::::::::::::::::::::::::::::::: solution

One reasonable design is `item_id` (unique string), `title` (string), `author` (string), and `publication_year` (integer or null). If the year is unknown, use a missing value rather than inventing a year. Other designs are valid if the rules are explicit.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 4. CSV and TSV: structured text in rows

**CSV** means *comma-separated values*. **TSV** means *tab-separated values*. Both commonly represent a table, with a header row naming the fields.

CSV example (`data/activities.csv`):

```csv
id,activity,hours,completed
101,Literature review,2.5,true
102,Clean survey data,1.0,false
103,Draft report,3.0,false
```

TSV example (`output/activities.tsv`):

```tsv
id	activity	hours	completed
101	Literature review	2.5	true
102	Clean survey data	1.0	false
103	Draft report	3.0	false
```

In the TSV example, the spaces between fields represent **tab characters**, not ordinary spaces. A TSV file should use actual tabs.

CSV needs care when a value itself contains a comma, quote, or newline. For example:

```csv
id,activity,hours,completed
104,"Read, annotate, and summarize",1.5,false
```

Quotation marks allow the comma to remain part of the `activity` value. A proper CSV reader handles this; simply splitting every line at each comma can break valid data.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Predict the error (5 minutes)

An AI agent is asked to split each CSV line using the comma character. What could go wrong with the row containing `"Read, annotate, and summarize"`? What should you ask the agent to use instead?

:::::::::::::::::::::::::::::::::::::::: solution

A naive split produces too many fields because the activity contains commas. Ask the agent to use a standards-aware CSV parser (such as Python's built-in `csv` module), preserve the header, and check the number of fields in each record.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 5. JSON: structured data with types and nesting

**JSON** (JavaScript Object Notation) represents information using objects, arrays, strings, numbers, Booleans, and `null`.

The same activities can be represented as an array of objects:

```json
[
  {"id": 101, "activity": "Literature review", "hours": 2.5, "completed": true},
  {"id": 102, "activity": "Clean survey data", "hours": 1.0, "completed": false},
  {"id": 103, "activity": "Draft report", "hours": 3.0, "completed": false}
]
```

JSON uses double quotes around field names and strings. Boolean values are lowercase `true` and `false`. Unlike CSV, JSON can naturally represent nested information:

```json
{
  "project": "Research tracker",
  "activities": [
    {"id": 101, "tags": ["reading", "planning"]}
  ]
}
```

JSON is common in APIs and application data exchange. It is not always the easiest format for humans to edit by hand.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Read JSON (5 minutes)

Consider:

```json
{"name": "Sample A", "scores": [8, 10], "reviewed": false}
```

1. Which value is an array?
2. Which value is a Boolean?
3. Is `"8"` equivalent to the number `8`?

:::::::::::::::::::::::::::::::::::::::: solution

1. `scores` contains an array.
2. `reviewed` contains a Boolean.
3. No. `"8"` is a string, while `8` is a number.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 6. YAML: readable configuration

**YAML** is commonly used for configuration files, including the `config.yaml` in this Carpentries Workbench repository.

```yaml
project: Research tracker
output_directory: output
include_completed: false
fields:
  - id
  - activity
  - hours
  - completed
```

YAML uses indentation to show structure. A list item begins with `-`. YAML can be convenient for people editing settings, but indentation and ambiguous scalar values can lead to mistakes. When a value must be treated as text, quoting it is often safer:

```yaml
participant_id: "0007"
report_date: "2026-10-27"
```

Do not confuse a configuration file with a dataset. YAML can represent datasets too, but its most common role in this course is to describe settings and instructions for tools.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Inspect a configuration (5 minutes)

What do these settings instruct an application to do?

```yaml
source_file: data/activities.csv
output_file: output/activities.json
skip_completed: true
```

What important question should we ask before implementing `skip_completed`?

:::::::::::::::::::::::::::::::::::::::: solution

The application should read the CSV source and write JSON output, skipping records marked completed. We should clarify how completion is represented in the CSV (for example, the text `true` or `false`), how missing values are handled, and whether the original file must remain unchanged.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 7. Converting between formats: preserve meaning

Suppose a collaborator wants JSON, but your source is CSV. The task is not merely to change the filename extension. A real conversion must read one format, interpret its fields, and write the other format.

A useful workflow is:

```text
START

Read data/activities.csv using a CSV parser
Check that required columns are present
FOR EACH row:
    Read id, activity, hours, completed
    Convert id to the agreed ID type
    Convert hours to a number
    Convert completed to a Boolean
    IF a required value is invalid:
        Record the error and stop or flag the row
    ELSE:
        Add a structured record to the result
Write the result to output/activities.json
Read the JSON output again to verify it is valid
Check record count and representative values
Report any rejected records or conversions

END
```

Before implementing, agree on the rules. In our example, IDs are numbers, but in a real project IDs might be strings. Also decide how to handle blank cells, duplicates, and malformed values.

### A verification checklist

- Does the output file exist at the expected path?
- Is the output syntactically valid?
- Is the number of records as expected?
- Are the field names correct?
- Have types been converted as intended?
- Were leading zeros, commas, and missing values preserved appropriately?
- Was the original file left unchanged?

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Spot the conversion bug (5 minutes)

A conversion script turns this CSV row:

```csv
participant_id,completed
0007,false
```

into this JSON:

```json
{"participant_id": 7, "completed": "false"}
```

Identify two problems and propose the correct JSON record.

:::::::::::::::::::::::::::::::::::::::: solution

The ID lost its leading zeros, and the Boolean was converted into a string. If the ID is defined as text, a suitable output is:

```json
{"participant_id": "0007", "completed": false}
```

::::::::::::::::::::::::::::::::::::::::::::::::::

## 8. Asking an AI coding agent to convert data

Compare these two instructions.

**Vague request:**

> Convert my data to JSON.

**Structured request:**

> In this project, read `data/activities.csv` and write `output/activities.json`. The CSV has the columns `id`, `activity`, `hours`, and `completed`. Treat `id` as an integer for this particular dataset, `activity` as text, `hours` as a decimal number, and `completed` as a Boolean represented by the strings `true` or `false` in CSV. Use a proper CSV parser. Do not overwrite the source. If a row contains an invalid value, report its row number rather than guessing. After conversion, validate the JSON, confirm the record count, and show the first converted record. Explain the steps you plan to take before writing code.

The second request provides paths, format rules, type rules, error handling, and tests. It is easier to implement and evaluate.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Build and verify (10 minutes)

Use an AI coding agent (or work in pairs with an instructor) to:

1. Create `data/activities.csv` using the three example records at the start of this lesson.
2. Ask the agent to convert it to `output/activities.json` using the structured request above.
3. Inspect the generated JSON.
4. Add a fourth CSV row with an invalid value for `hours`, such as `unknown`.
5. Run the conversion again. Does the agent's implementation report the error, or does it silently produce incorrect data?

**Reflection:** What additional instruction would improve the implementation or its verification?

:::::::::::::::::::::::::::::::::::::::: solution

Expected behaviour: the first conversion produces three JSON objects with numeric `id` and `hours` values and Boolean `completed` values. The invalid fourth row should be reported clearly with its row number; it should not be silently converted to `0` or omitted without explanation. Depending on the implementation, the conversion may stop or collect errors, but that policy should be explicit.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 9. Independent challenge: design an exchange format

A researcher wants to share a list of reading materials with a collaborator. Each record includes a unique identifier, title, publication year (sometimes unknown), and tags (possibly several).

Before prompting an AI agent:

1. Propose a folder structure and filenames.
2. Define each field and its type.
3. Choose CSV, TSV, JSON, or YAML as the primary exchange format and justify your choice.
4. Write one example record.
5. Describe how you would verify that a conversion preserved all tags and missing publication years.

:::::::::::::::::::::::::::::::::::::::: solution

One reasonable choice is JSON because `tags` is naturally an array:

```json
{
  "item_id": "R-001",
  "title": "Example reading",
  "publication_year": null,
  "tags": ["methods", "review"]
}
```

A CSV design is also possible, but learners must decide how to encode multiple tags within one field and how to recover them reliably. The key is to make those rules explicit.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Wrap-up: a reusable way to describe data tasks

Before asking an AI agent to work with data, answer these questions:

1. **Where?** What are the input and output file paths?
2. **What format?** CSV, TSV, JSON, YAML, or something else?
3. **What structure?** Which records, fields, and nested values exist?
4. **What types?** Which values are text, numbers, Booleans, or missing?
5. **What transformation?** What should change and what must stay the same?
6. **What exceptions?** How should malformed or missing data be handled?
7. **How to verify?** What checks demonstrate that the result is correct?

:::::::::::::::::::::::::::::::::::::::: instructor

### Instructor notes

**Preparation:** Have a sample project folder ready with `data/activities.csv`, an empty `output/` directory, and a text editor. If using an AI coding agent, test the exercise in the teaching environment beforehand. Learners do not need to write conversion code themselves.

**Live demonstration:** Open the same records in CSV and JSON. Ask learners to predict what will change before showing the result. Show a path error and a malformed CSV row. Emphasize that changing `.csv` to `.json` in a filename is not conversion.

**Common misconceptions:**

- An extension guarantees file contents are valid.
- CSV stores numbers and Booleans with the same type information as JSON.
- A record is the same as a field.
- A missing value is equivalent to zero or an empty string.
- A successful script run proves the converted data is correct.
- All IDs should be converted to numbers.

**Formative checks:** Ask learners to identify a relative path, predict the effect of an embedded comma in CSV, recognize a JSON Boolean, and explain why an ID with leading zeros should remain text.

**Timing:** The episode is planned for 85 minutes of teaching and 35 minutes of exercises (120 minutes total). Exercises may be shortened for a 90-minute workshop.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Files live in directories and are located using paths; extensions are clues, not guarantees.
- Tables organize records into fields, and values have types that affect their meaning.
- CSV and TSV are common tabular text formats; JSON supports typed and nested structures; YAML is often used for configuration.
- Converting data requires parsing, explicit type rules, error handling, and verification.
- A good AI coding request specifies input and output paths, data structure, transformation rules, and acceptance checks.

::::::::::::::::::::::::::::::::::::::::::::::::::

