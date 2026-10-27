---
title: "Data, Files and Structured Information"
teaching: 85
exercises: 35
---

:::::::::::::::::::::::::::::::::::::::: questions

- How does software represent, store, and exchange information?
- How can I describe a file's structure to an AI coding agent?
- How can I check whether a conversion preserved the meaning of my data?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

- Navigate project directories and interpret file paths.
- Distinguish file extensions, formats, and contents.
- Identify common data types, records, and fields.
- Read CSV, TSV, JSON, and YAML.
- Specify and verify a data-conversion workflow for an AI coding agent.

::::::::::::::::::::::::::::::::::::::::

## Introduction: the same information, different representations

Imagine collecting research activities in a spreadsheet, then asking an AI coding agent to display them on a website. Before asking the agent to write code, you need to know **where the data is**, **how it is organized**, and **what each value means**.

We will use the same small dataset throughout this episode:

| id | activity | hours | completed |
| --- | --- | ---: | --- |
| 101 | Literature review | 2.5 | true |
| 102 | Clean survey data | 1.0 | false |
| 103 | Draft report | 3.0 | false |

:::::::::::::::::::::::::::::::::::::::: callout

### Why this matters for vibe coding

An AI agent may guess a file path, treat an identifier as a number, misread a comma inside a CSV value, or silently drop missing information. Knowing the structure of your data helps you specify the task and check the result.

::::::::::::::::::::::::::::::::::::::::

## 1. Files, directories, and paths

A **file** stores information. A **directory** (folder) organizes files. A **path** tells software where to find a file.

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

From the `research-tracker/` directory, `data/activities.csv` is a **relative path**. An **absolute path**, such as `/home/learner/research-tracker/data/activities.csv`, specifies a location from the filesystem root. Relative paths depend on the working directory; absolute paths often differ between computers.

An extension such as `.csv` suggests a file format but does not guarantee that its contents are valid CSV.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Find the file (5 minutes)

Assume your working directory is `research-tracker/`.

1. What is the relative path to `activities.json`?
2. Where could you save a generated `activities.tsv` without overwriting the source?
3. If you move into `scripts/`, what relative path reaches `activities.csv`?

:::::::::::::::::::::::::::::::::::::::: solution

1. `data/activities.json`
2. `output/activities.tsv`
3. `../data/activities.csv` (`..` means the parent directory).

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2. Data types: what does a value mean?

A **data type** tells software what kind of value it is handling.

| Type | Example | Meaning |
| --- | --- | --- |
| String | `"00101"` | Text, including identifiers |
| Integer | `101` | Whole number |
| Decimal number | `2.5` | Numeric quantity |
| Boolean | `true` | True or false |
| Missing/null | `null` | No value present |
| Array/list | `["review", "write"]` | Ordered collection |
| Object/mapping | `{"hours": 2.5}` | Named fields and values |

The text `"101"` and the number `101` are different. An identifier such as `"00101"` should usually remain text to preserve leading zeros. The text `"false"` is not the Boolean `false`.

CSV and TSV represent fields as text; conversion to numbers or Booleans requires explicit rules. JSON supports several types directly. YAML supports typed values too, but parsing conventions can vary.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Choose a type (5 minutes)

Choose a suitable type for each item and explain any ambiguity:

1. Participant ID `"0007"`
2. Number of responses `42`
3. Whether consent was recorded
4. Date `2026-10-27`
5. Unknown age

:::::::::::::::::::::::::::::::::::::::: solution

1. String, to preserve leading zeros.
2. Integer.
3. Boolean if yes/no is sufficient; otherwise account for unknown status.
4. Standardized date string or a date type in systems that support it. JSON has no native date type.
5. Missing/null, not zero.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Tables, records, and fields

A **table** organizes information in rows and columns. A **record** is an item or observation (often a row). A **field** is a named attribute (often a column).

The first record in our example has `id = 101`, `activity = Literature review`, `hours = 2.5`, and `completed = true`.

Before asking an AI agent to process a table, decide which fields are required, which identify a record uniquely, and how missing or duplicate values should be handled.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Design a record (5 minutes)

You want to track reading materials. Propose four fields for each record. Which field uniquely identifies a record? What if the publication year is unknown?

:::::::::::::::::::::::::::::::::::::::: solution

One possible design: `item_id` (unique string), `title` (string), `author` (string), and `publication_year` (integer or null). Other designs are valid if their rules are clear.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 4. CSV and TSV: tabular text

**CSV** stands for comma-separated values; **TSV** stands for tab-separated values. They commonly include a header row.

CSV (`data/activities.csv`):

```csv
id,activity,hours,completed
101,Literature review,2.5,true
102,Clean survey data,1.0,false
103,Draft report,3.0,false
```

TSV uses actual tab characters between fields:

```tsv
id	activity	hours	completed
101	Literature review	2.5	true
102	Clean survey data	1.0	false
103	Draft report	3.0	false
```

CSV values can contain commas when properly quoted:

```csv
id,activity,hours,completed
104,"Read, annotate, and summarize",1.5,false
```

A naive operation that splits each line at every comma would incorrectly divide that activity into multiple fields. Use a proper CSV parser.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Predict the error (5 minutes)

What goes wrong if an AI agent splits the last CSV row on every comma? What should you ask it to do instead?

:::::::::::::::::::::::::::::::::::::::: solution

It produces too many fields. Ask the agent to use a standards-aware CSV parser, preserve the header, and validate the number of fields in each record.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 5. JSON: typed and nested information

**JSON** represents objects, arrays, strings, numbers, Booleans, and `null`.

```json
[
  {"id": 101, "activity": "Literature review", "hours": 2.5, "completed": true},
  {"id": 102, "activity": "Clean survey data", "hours": 1.0, "completed": false},
  {"id": 103, "activity": "Draft report", "hours": 3.0, "completed": false}
]
```

JSON field names and strings use double quotes. JSON can also nest arrays and objects:

```json
{
  "project": "Research tracker",
  "activities": [{"id": 101, "tags": ["reading", "planning"]}]
}
```

JSON is widely used for APIs and data exchange.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Read JSON (5 minutes)

```json
{"name": "Sample A", "scores": [8, 10], "reviewed": false}
```

1. Which value is an array?
2. Which is a Boolean?
3. Is `"8"` equivalent to `8`?

:::::::::::::::::::::::::::::::::::::::: solution

1. `scores`.
2. `reviewed`.
3. No: `"8"` is text and `8` is a number.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 6. YAML: readable configuration

**YAML** is often used to describe settings, including in a Carpentries Workbench `config.yaml` file.

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

Indentation expresses structure. A dash starts a list item. Quote values that must remain strings, especially identifiers with leading zeros and date-like text:

```yaml
participant_id: "0007"
report_date: "2026-10-27"
```

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Inspect a configuration (5 minutes)

```yaml
source_file: data/activities.csv
output_file: output/activities.json
skip_completed: true
```

What does this configuration instruct a program to do? What must be clarified before implementing `skip_completed`?

:::::::::::::::::::::::::::::::::::::::: solution

Read the CSV and write JSON, excluding completed records. Clarify how the CSV represents completion, what to do with missing values, and whether the source must remain unchanged.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 7. Converting between formats: preserve meaning

Renaming `.csv` to `.json` is not conversion. A conversion must **parse** the source, interpret fields, and **serialize** the result into the target format.

```text
START
Read data/activities.csv with a CSV parser
Check that required columns are present
FOR EACH row:
    Read id, activity, hours, completed
    Convert id according to the agreed identifier rule
    Convert hours to a number
    Convert completed to a Boolean
    IF a required value is invalid:
        Report its row number and stop or flag the row
    ELSE:
        Add the converted record to the result
Write the result to output/activities.json
Read the output again and validate its JSON syntax
Check record count and representative values
Report errors and rejected records
END
```

Decide the handling of missing values, duplicate IDs, invalid numbers, and malformed rows **before** asking the AI to write the converter.

### Verification checklist

- Does the output exist at the correct path?
- Is the output valid JSON?
- Are record counts and field names correct?
- Are data types correct?
- Are identifiers and missing values preserved as intended?
- Is the original source unchanged?

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Spot the conversion bug (5 minutes)

A converter turns this CSV:

```csv
participant_id,completed
0007,false
```

into:

```json
{"participant_id": 7, "completed": "false"}
```

Identify two problems and propose the correct JSON.

:::::::::::::::::::::::::::::::::::::::: solution

The ID lost leading zeros, and the Boolean became text. If IDs are defined as strings:

```json
{"participant_id": "0007", "completed": false}
```

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 8. Asking an AI coding agent to convert data

Compare these instructions.

**Vague request:**

> Convert my data to JSON.

**Structured request:**

> Read `data/activities.csv` and write `output/activities.json`. The CSV contains `id`, `activity`, `hours`, and `completed`. For this dataset, convert `id` to an integer, `activity` to text, `hours` to a decimal number, and `completed` from the CSV text `true`/`false` to a Boolean. Use a proper CSV parser. Do not overwrite the source. Report the row number of any invalid value rather than guessing. Validate the JSON, check the record count, and show the first converted record. Explain your plan before writing code.

The structured request makes the paths, types, errors, and acceptance checks explicit.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Build and verify (10 minutes)

1. Create `data/activities.csv` using the three example records.
2. Ask an AI coding agent to convert it using the structured request.
3. Inspect the resulting JSON.
4. Add a fourth row with `hours` set to `unknown`.
5. Run the conversion again. Does it report the error or silently produce incorrect data?

**Reflection:** What additional instruction would make the implementation safer?

:::::::::::::::::::::::::::::::::::::::: solution

The first run should produce three JSON records with numeric `id` and `hours` and Boolean `completed` values. The second run should report the invalid fourth row. Whether the conversion stops or collects errors is a policy to specify; it must not silently replace invalid data with zero.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 9. Independent challenge: design an exchange format

A researcher wants to share reading materials. Each record has a unique ID, title, publication year (possibly unknown), and several tags.

Before prompting an AI agent:

1. Propose a folder structure and filenames.
2. Define each field and its type.
3. Choose CSV, TSV, JSON, or YAML and justify your choice.
4. Write one example record.
5. Describe how to verify that a conversion preserves all tags and missing years.

:::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Choose and justify a format

Work independently, then compare your design with a partner. Can your partner interpret your data without guessing?

:::::::::::::::::::::::::::::::::::::::: solution

JSON is a reasonable choice because `tags` can be an array:

```json
{
  "item_id": "R-001",
  "title": "Example reading",
  "publication_year": null,
  "tags": ["methods", "review"]
}
```

CSV is also possible, but the encoding of multiple tags in a field must be specified and reversible.

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## Wrap-up: describe a data task before implementing it

Before asking an AI coding agent to work with files, answer: **Where are the files? What formats and structures do they use? What types do fields represent? What transformation is needed? What must be preserved? What could go wrong? How will you verify the output?**

:::::::::::::::::::::::::::::::::::::::: instructor

### Instructor notes

**Preparation:** Have `data/activities.csv`, an empty `output/` folder, and a text editor ready. Test the conversion exercise with the intended AI coding agent beforehand.

**Live demonstration:** Compare CSV and JSON representations of the same records. Ask learners to predict which values change type. Show a missing-path error and a CSV field containing commas.

**Common misconceptions:** A file extension guarantees its format; CSV preserves numeric types; missing means zero; IDs must always be numbers; a script finishing without errors proves its output is correct.

**Formative checks:** Ask learners to identify relative paths, explain CSV quoting, distinguish JSON strings from Booleans, and describe how to preserve leading zeros.

**Timing:** 85 minutes teaching and 35 minutes exercises (120 minutes total). For a shorter workshop, assign the independent challenge as homework.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Files are organized into directories and identified using paths.
- Extensions suggest formats but do not validate contents.
- Tables contain records and fields; values have types that affect meaning.
- CSV and TSV represent tabular text; JSON supports nested typed values; YAML commonly describes configuration.
- Data conversion requires parsing, explicit type rules, error handling, and verification.
- A useful AI coding request specifies input and output paths, transformation rules, and acceptance checks.

::::::::::::::::::::::::::::::::::::::::
