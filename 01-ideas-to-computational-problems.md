---
title: "From Ideas to Computational Problems"
teaching: 90
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I describe what I want in a way that a computer or AI agent can implement?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Break a larger task into smaller, ordered steps.
- Identify inputs, outputs, variables, and state.
- Describe conditions, loops, functions, dependencies, and data flow.
- Write pseudocode for a simple application.
- Use pseudocode to guide and verify an AI-generated implementation.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Imagine asking an AI coding agent:

> Build me an application to manage my daily tasks.

The agent may produce a working-looking application, but what does *manage* mean? Can users add tasks, complete them, delete them, or keep them after refreshing the page? If we do not specify these details, the agent will make assumptions.

In this lesson, we will turn an idea into a **computational workflow** and then into **pseudocode** that another person or an AI coding agent can implement and test. Our running example is a simple task manager.

## 1. From an Idea to a Computational Problem (10 minutes)

A computational problem can be described in terms of information, operations, decisions, and expected results. Before building, ask what the application must actually do.

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: What's missing? (3 minutes)

A friend says, "I want an application to manage my daily tasks." Write three questions you would ask before implementing it. Compare your questions with a partner.

:::::::::::::::::::::::::::::::: solution

### Example discussion

- What information is required to add a task?
- What happens when a task is marked complete?
- Should tasks remain available after the page is refreshed?
- What happens if someone tries to add an empty task?

There is no single correct list: the purpose is to uncover hidden assumptions.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

**Key idea:** Computers require explicit behaviour. AI agents can guess, but their guesses may not match your intentions.

## 2. Breaking a Problem into Smaller Steps (15 minutes)

**Decomposition** means dividing a large task into smaller responsibilities. A task manager might need to add, display, complete, and delete tasks. Start with one feature: adding a task.

```text
1. User enters a task description
2. User clicks Add
3. Application checks the description
4. Application saves a valid task
5. Application displays the updated task list
```

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Complete a task (5 minutes)

Write the steps that should happen when a user marks a task as completed. Which steps must happen in a particular order?

:::::::::::::::::::::::::::::::: solution

```text
1. User selects a task
2. User clicks Complete
3. Application identifies the selected task
4. Application changes its completed status to true
5. Application saves the updated task
6. Application refreshes the displayed task list
```

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 3. Inputs, Outputs, Variables, and State (15 minutes)

An **input** is information supplied to a process; an **output** is what the process produces.

| Part | Add Task example |
| --- | --- |
| Input | Task description |
| Process | Validate and save the task |
| Output | Updated task list or an error message |

A **variable** names a value used by the program:

```text
task_description = "Submit assignment"
task_completed = false
task_priority = "High"
```

**State** is the information that represents the application's current situation. For example, a list of tasks and their completion statuses is part of the task manager's state. When a task is added or completed, state changes.

**Persistence** is different: if tasks must survive a refresh or restart, the application must store them and reload them later.

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Identify state (3 minutes)

For a shopping-list app, identify two pieces of information the app must remember. Which information should survive closing the browser?

:::::::::::::::::::::::::::::::: solution

The app remembers each item's name and whether it has been purchased. If users expect to return later, the list and purchased statuses should be saved persistently.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 4. Conditions and Decision-Making (15 minutes)

A **condition** determines which action happens based on a question with a true/false result. What if the user clicks Add without entering anything?

```text
IF task_description is empty or whitespace only
    SHOW "Please enter a task"
ELSE
    SAVE the task
```

The workflow branches: invalid input produces an error; valid input produces a saved task.

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Priority warning (4 minutes)

Write pseudocode for this rule: If a task has high priority, display a warning; otherwise, display the task normally.

:::::::::::::::::::::::::::::::: solution

```text
IF task_priority is "High"
    DISPLAY priority warning
ELSE
    DISPLAY task normally
```

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 5. Repetition and Loops (10 minutes)

Suppose the app has 100 tasks. We should not write 100 separate display instructions. A **loop** describes an operation that repeats:

```text
FOR EACH task IN saved_tasks
    DISPLAY task
```

Look for phrases such as *each*, *every*, *repeat*, or *until* when analyzing a task.

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Spot repetition (3 minutes)

Which tasks involve repetition?

1. Display every product in an online shop.
2. Check whether one password is empty.
3. Calculate the total price of all items in a basket.
4. Change a page title once.

:::::::::::::::::::::::::::::::: solution

Tasks 1 and 3 naturally involve repetition over collections. Tasks 2 and 4 do not inherently require a loop.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 6. Functions: Naming Smaller Jobs (10 minutes)

A **function** is a named, reusable operation with a clear responsibility. We can describe the task manager using jobs such as:

```text
validateTask(description)
saveTask(task)
displayTasks()
completeTask(task_id)
```

A function may accept information and return a result:

```text
FUNCTION validateTask(description)
    IF description is empty or whitespace only
        RETURN false
    ELSE
        RETURN true
END FUNCTION
```

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Name the jobs (3 minutes)

Suggest three functions for an expense tracker that records expenses and calculates total spending.

:::::::::::::::::::::::::::::::: solution

`validateAmount()`, `addExpense()`, and `calculateTotal()` are possible choices. Other sensible designs are acceptable.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 7. Dependencies and Data Flow (10 minutes)

Some steps cannot happen until earlier steps have finished. For example, we cannot validate a description before reading it, and we should not save an invalid description.

```text
Read description
       |
       v
Validate description
       |
       v
Save valid task
       |
       v
Update task list
```

These ordering requirements are **dependencies**. **Data flow** describes where information comes from, how operations use or change it, and where results go.

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Fix the order (3 minutes)

Put these actions in a sensible order: `display updated list`, `validate description`, `read description`, `save task`.

:::::::::::::::::::::::::::::::: solution

Read description -> validate description -> save valid task -> display updated list. If validation fails, show an error instead of saving.

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 8. Writing Pseudocode (15 minutes)

**Pseudocode** expresses a workflow in readable, structured language without requiring the syntax of a specific programming language. It combines the concepts we have learned:

```text
START TASK MANAGER

LOAD saved tasks
FOR EACH task IN saved tasks
    DISPLAY task

WHEN user clicks Add
    READ task description
    IF description is empty or whitespace only
        SHOW error
    ELSE
        CREATE task with completed = false
        SAVE task
        DISPLAY updated task list

WHEN user marks a task complete
    FIND selected task
    IF task exists
        SET completed = true
        SAVE updated task
        DISPLAY updated task list
    ELSE
        SHOW "Task not found"

END TASK MANAGER
```

| Pseudocode element | Concept |
| --- | --- |
| `READ task description` | Input |
| `description` | Variable |
| `IF description is empty` | Condition |
| `FOR EACH task` | Loop |
| `completed` | State |
| `SAVE updated task` | Operation/function |
| Validate before save | Dependency |
| Read -> validate -> save -> display | Data flow |

::::::::::::::::::::::::::::::::::::::: challenge

### Challenge: Add deletion (5 minutes)

Write pseudocode for deleting a selected task. Consider what happens if the task cannot be found.

:::::::::::::::::::::::::::::::: solution

```text
WHEN user clicks Delete
    IDENTIFY selected task
    IF task exists
        REMOVE task from saved tasks
        SAVE updated task list
        DISPLAY updated task list
    ELSE
        SHOW "Task not found"
```

::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 9. From Pseudocode to an AI Coding Agent (10 minutes)

We will compare two prompts in the same AI coding environment.

**Experiment A: Vague prompt**

> Build me a simple task manager.

Run the result. Record what the agent decided without asking you: supported features, validation, saving, and interface behaviour.

**Experiment B: Structured prompt**

> Build a simple browser-based task manager using HTML, CSS, and JavaScript. Users must be able to add, complete, and delete tasks. Each task has a unique ID, description, and completed status. Reject empty or whitespace-only descriptions with an error message. Save tasks in browser localStorage and load them when the page opens. Update the displayed list after each change. First explain your plan briefly, then implement. Do not add extra features. Explain how to test the main behaviours.

Compare the implementations:

| Question | Vague prompt | Structured prompt |
| --- | --- | --- |
| Were intended features implemented? | | |
| Were important behaviours missing? | | |
| Did the agent make unexpected assumptions? | | |
| Can you verify the result? | | |

**Important:** A detailed specification does not guarantee correct software. It makes intended behaviour easier to communicate and test.

## 10. Independent Challenge: Expense Tracker (10 minutes; extend as homework)

**Scenario:** Build an application that lets users record expenses and see how much they have spent.

Before asking an AI agent to code, complete this worksheet:

| Question | Your answer |
| --- | --- |
| Goal: What should the app achieve? | |
| Inputs: What does the user provide? | |
| Outputs: What should appear? | |
| Steps: What happens when an expense is added? | |
| Variables and state: What must be remembered? | |
| Conditions: What decisions are needed? | |
| Loops: What repeats? | |
| Functions: What smaller jobs are needed? | |
| Dependencies: What must happen first? | |

Next, write pseudocode, ask an AI coding agent to implement it, and test these cases:

1. Add a valid expense.
2. Try to add an expense without an amount.
3. Add multiple expenses and verify the total.

**Reflection:** What did the AI implement differently from what you expected? How would you change your specification?

:::::::::::::::::::::::::::::::::::: instructor

## Instructor Notes

**Teaching approach:** Build the task-manager workflow live with learners. Ask for predictions and learner suggestions before showing solutions. Keep explanations short and alternate them with exercises.

**Common misconceptions:**

- "AI will figure out what I mean." Ask which assumptions the agent made.
- "Pseudocode must look like real code." Emphasize clarity rather than syntax.
- "Every step must be a function." Prefer functions with meaningful responsibilities.
- "State means a database." Contrast in-memory state with persistent storage.
- "If the AI produces an app, the task is complete." Require behavioural tests.

**Formative checkpoints:**

- Can another person follow the workflow without guessing?
- What happens with missing or invalid input?
- What repeats when there are 100 items instead of three?
- Which operations depend on earlier results?
- What example would prove that the feature works?

**Exit ticket:** Describe the inputs, outputs, state, decisions, repetition, and main steps of a meal recommender that uses ingredients already available at home.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- Start by clarifying the goal, inputs, and expected outputs.
- Decompose a large task into smaller, ordered operations.
- Use variables and state to describe the information the application works with and remembers.
- Use conditions for decisions and loops for repeated operations.
- Use functions to name meaningful, reusable jobs.
- Track dependencies and data flow to ensure the workflow makes sense.
- Use pseudocode to communicate behaviour before implementing it.
- Test AI-generated implementations against explicit examples and refine the specification when needed.

::::::::::::::::::::::::::::::::::::::::::::::::
