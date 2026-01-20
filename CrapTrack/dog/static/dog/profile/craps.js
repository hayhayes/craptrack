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

export function show_craps(craps, page, dogs) {
  if(page){
    setPage(page, "Craps");
  }

  const addBtn = createButton("Add Crap +", () => add_form("crap"));
  const form = createCrapForm(dogs);

  const responsiveDiv = document.createElement("div");
  responsiveDiv.className = "table-responsive";

  const { table, tbody } = createTable(["Date", "Type", "Color", "Dog"]);
    table.id = 'crap-table';

  responsiveDiv.appendChild(table);

  page.dashboard.append(addBtn, form, responsiveDiv);

  if (craps) {
    renderRows(
      tbody,
      craps.map(c => [
        new Date(c.datetime).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
        }),
        c.crap_type,
        c.color,
        c.dog_name,
      ]),
    );
  }
}

function createCrapForm(dogs) {
  const form = document.createElement("form");
  form.id = "crap";
  form.style.display = "none";
  form.className = "mb-4";

  // Dog
  form.appendChild(createSelect("dog", "Dog", dogs.map((dog) => ({name: dog.name, id: dog.id}))));

  // Date
  form.appendChild(createInput("date", "datetime-local", "Date"));

  // Poo Type
  const img = document.createElement("img");
  img.src = chartImgUrl;
  const div = document.createElement("div");
  div.className="row poo-type";
  const select = createSelect("type", "Type", [1, 2, 3, 4, 5, 6, 7]);
  select.classList.add("ml-4", "align-self-center");
  div.append(img, select);
  form.appendChild(div);

  // color
  form.appendChild(createSelect("color", "Color", ["Brown", "Black", "Green", "White", "Yellow", "Red"]));

  // Submit button
  const submit = document.createElement("button");
  submit.type = "submit";
  submit.className = "btn btn-success mt-3";
  submit.textContent = "Save Crap";

  form.appendChild(submit);

  form.addEventListener("submit", handleCrapSubmit);

  return form;
}

export async function handleCrapSubmit(e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  try {
    const res = await fetch("/crap", {
      method: "POST",
      body: formData,
    });

    if (!res.ok) throw new Error("Failed to save crap");

    const newCrap = await res.json();

    // Append new row to table
    const tbody = document.querySelector("#crap-table tbody"); // make sure your table has this ID
    const tr = document.createElement("tr");

    [
      new Date(newCrap.date).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
      }),,
      newCrap.type,
      newCrap.color,
      newCrap.dog_name
    ].forEach(text => {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    });

    tbody.appendChild(tr);

    // Reset and hide form
    form.reset();
    form.style.display = "none";

  } catch (err) {
    alert(err.message);
    console.error(err);
  }
}

