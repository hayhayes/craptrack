import {
  createButton,
  createSelect,
  createTable,
  renderRows,
  createInput,
  add_form,
  addOptions,
  setPage
} from './helpers.js';

export function show_activities(activities, page, dogs) {
  if(page){
    setPage(page, "Daily Activity");
  }

  const addBtn = createButton("Add Activity +", () => add_form("activity"));
  const form = createActivityForm(dogs);

  const responsiveDiv = document.createElement("div");
  responsiveDiv.className = "table-responsive";

  const { table, tbody } = createTable(["Date", "Intensity", "Length", "Dog"]);
  table.id = 'activities-table';

  responsiveDiv.appendChild(table);

  page.dashboard.append(addBtn, form, responsiveDiv);

  if (activities) {
    renderRows(
      tbody,
      activities.map(a => [
        new Date(a.datetime).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
        }),
        a.activity,
        a.intensity,
        a.minutes,
        a.dog_name,
      ])
    );
  }
}

function createActivityForm(dogs) {
  const form = document.createElement("form");
  form.id = "activity";
  form.style.display = "none";
  form.className = "mb-4";

  // Dog
  form.appendChild(createSelect("dog", "Dog", dogs.map((dog) => ({name: dog.name, id: dog.id}))));

  // Date
  form.appendChild(createInput("date", "datetime-local", "Date"));

  // Activity
  form.appendChild(createInput("activity", "text", "Activity"));

  // Intensity
  form.appendChild(createSelect("intensity", "Intensity", [
    "low",
    "medium",
    "high",
  ]));

  // Length
  form.appendChild(createInput("minutes", "number", "Length in Minutes"));

  // Submit button
  const submit = document.createElement("button");
  submit.type = "submit";
  submit.className = "btn btn-success mt-3";
  submit.textContent = "Save Activity";

  form.appendChild(submit);

  form.addEventListener("submit", handleActivitySubmit);

  return form;
}

async function handleActivitySubmit(e) {
  e.preventDefault();

  const formData = new FormData(e.target);

  try {
    const response = await fetch("/activity", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Failed to save activity");
    }

    const newActivity = await response.json();

    const tbody = document.querySelector("#activities-table tbody");
    const tr = document.createElement("tr");

    [
      new Date(newActivity.datetime).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
      }),
      newActivity.activity,
      newActivity.intensity,
      newActivity.minutes,
      newActivity.dog_name
    ].forEach(text => {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    });

    tbody.appendChild(tr);

    // Reset and hide form
    e.target.reset();
    e.target.style.display = "none";

  } catch (err) {
    alert(err.message);
    console.error(err);
  }
}

