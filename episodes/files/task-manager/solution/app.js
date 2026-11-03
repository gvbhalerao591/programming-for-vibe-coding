import { loadTasks, saveTasks } from "../storage.js";

let tasks = loadTasks();
const form = document.querySelector("form");
const input = document.querySelector("#description");
const message = document.querySelector("#message");
const list = document.querySelector("#tasks");

// The solution also rejects descriptions containing only whitespace.
function validateTask(description) {
  return description.trim().length > 0;
}

function addTask(description) {
  if (!validateTask(description)) {
    message.textContent = "Please enter a task.";
    return;
  }
  const task = { id: crypto.randomUUID(), description, completed: false };
  tasks.push(task);
  saveTasks(tasks);
  displayTasks();
  message.textContent = "Task added.";
  form.reset();
}

function displayTasks() {
  list.replaceChildren();
  for (const task of tasks) {
    const row = document.createElement("li");
    const label = document.createElement("span");
    label.textContent = task.description + (task.completed ? " (complete)" : "");
    const complete = document.createElement("button");
    complete.textContent = task.completed ? "Reopen" : "Complete";
    complete.addEventListener("click", () => {
      task.completed = !task.completed;
      saveTasks(tasks);
      displayTasks();
    });
    const remove = document.createElement("button");
    remove.textContent = "Delete";
    remove.addEventListener("click", () => {
      tasks = tasks.filter((item) => item.id !== task.id);
      saveTasks(tasks);
      displayTasks();
    });
    row.append(label, complete, remove);
    list.append(row);
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  addTask(input.value);
});

document.querySelector("#reset").addEventListener("click", () => {
  tasks = [];
  saveTasks(tasks);
  displayTasks();
  message.textContent = "Practice tasks cleared.";
});

displayTasks();
