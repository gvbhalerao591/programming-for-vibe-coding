// This is a local module, not an installed third-party package.
// Each version uses its own key, so experiments do not mix their task lists.
const storageKey = "course-tasks-" + window.location.pathname;

export function loadTasks() {
  return JSON.parse(localStorage.getItem(storageKey) || "[]");
}

export function saveTasks(tasks) {
  localStorage.setItem(storageKey, JSON.stringify(tasks));
}
