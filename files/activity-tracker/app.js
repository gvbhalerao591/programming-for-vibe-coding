const form = document.querySelector("form");
const message = document.querySelector("#message");
const list = document.querySelector("#activities");

async function loadActivities() {
  const response = await fetch("/api/activities");
  if (!response.ok) throw new Error("Could not load activities.");
  const activities = await response.json();
  list.replaceChildren();
  for (const activity of activities) {
    const row = document.createElement("li");
    row.textContent = `${activity.activity}: ${activity.hours} hours`;
    list.append(row);
  }
}

function showError(error) {
  message.textContent = "Request failed: " + error.message;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const record = {
    activity: document.querySelector("#activity").value,
    hours: Number(document.querySelector("#hours").value),
  };
  try {
    const response = await fetch("/api/activities", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(record),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error);
    message.textContent = `Activity ${result.id} saved.`;
    form.reset();
  } catch (error) {
    showError(error);
    return;
  }
  try {
    await loadActivities();
  } catch (error) {
    message.textContent += " The list could not refresh. Try Reload list.";
  }
});

document.querySelector("#reload").addEventListener("click", () => {
  loadActivities().then(() => { message.textContent = "List reloaded."; }).catch(showError);
});
loadActivities().catch(showError);
