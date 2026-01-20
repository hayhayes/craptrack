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

export async function show_meals(meals, page, dogs) {
  if (page) {
    setPage(page, "Meals");
  }

  const addBtn = createButton("Add Meal +", () => add_form("meal"));
  const form = await createMealForm(dogs);

  const responsiveDiv = document.createElement("div");
  responsiveDiv.className = "table-responsive";

  const { table, tbody } = createTable(["Date", "Meal", "Food", "Amount", "Dog"], true);
  table.id = 'meals-table';

  responsiveDiv.appendChild(table);

  page.dashboard.append(addBtn, form, responsiveDiv);

  if (meals) {
    renderRows(
      tbody,
      meals.map(m => [
        new Date(m.datetime).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
        }),
        m.meal,
        m.food_name,
        m.amount,
        m.dog_name
      ]),
    {
      onEdit: (id) => openEditMealForm(id),
      onDelete: (id) => handleDeleteMeal(id)
    }
    );
  }
}

export async function createMealForm(dogs) {
  const form = document.createElement("form");
  form.id = "meal";
  form.style.display = "none";
  form.className = "mb-4";

  // Dog
  form.appendChild(createSelect("dog", "Dog", dogs.map((dog) => ({name: dog.name, id: dog.id}))));

  // Date
  form.appendChild(createInput("date", "datetime-local", "Date"));

  // Meal type
  form.appendChild(createSelect("meal", "Meal", [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snack"
  ]));

  // Brand
  const brandDiv = createSelect("brand", "Brand", []);
  const brandSelect = brandDiv.querySelector("select");
  try {
    const res = await fetch("/brands");
    const brands = await res.json();
    addOptions(brands, brandSelect);

    brandSelect.addEventListener('change', handleBrandChange);
    form.appendChild(brandDiv);

  } catch(err) {
    console.error(err);
    const option = document.createElement("option");
    option.textContent = "Failed to load brands";
    option.disabled = true;
    brandSelect.appendChild(option)
  }
  // Food
  form.appendChild(createSelect("food", "Food", []));

  // Amount
  form.appendChild(createInput("amount", "number", "Amount in Grams"));

  // Submit button
  const submit = document.createElement("button");
  submit.type = "submit";
  submit.className = "btn btn-success mt-3";
  submit.textContent = "Save Meal";

  form.appendChild(submit);

  // TODO:
  form.addEventListener("submit", handleMealSubmit);

  return form;
}

async function handleBrandChange(e){
  const fs = document.querySelector('select[name="food"]');
  fs.innerHTML = '';
  const brand = e.target.value;

  try{
    const res = await fetch(`/foods/${brand}`);
    const foods = await res.json();

    if (foods && foods.length){
      addOptions(foods, fs);
    } else {
      addOptions(["This brand does not currently have any food"], fs);
    }

  } catch(err) {
    console.error(err);
    const option = document.createElement("option");
    option.textContent = "Failed to load foods";
    option.disabled = true;
    fs.appendChild(option)
  }
}

export async function handleMealSubmit(e) {
  e.preventDefault();
  const form = document.querySelector("form#meal");
  const tbody = document.querySelector("#meals-table tbody");
  const tr = document.createElement("tr");
  const formData = new FormData(e.target);

  const mealId = form.dataset.mealId;
  const url = mealId ? `/meals/${mealId}/edit/` : "/meals";

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error("Failed to save meal");
    }

    const newMeal = await response.json();

    [
      new Date(newMeal.datetime).toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
      }),
      newMeal.meal,
      newMeal.food_name,
      newMeal.amount,
      newMeal.dog_name
    ].forEach(text => {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    });

    tbody.appendChild(tr);

    //delete form.dataset.mealId;
    e.target.reset();
    e.target.style.display = "none";

  } catch (err) {
    alert(err.message);
  }
}

export function openEditMealForm(meal) {
  const form = document.getElementById("meals-table");
  form.style.display = "block";

  form.dataset.mealId = meal.id;

  form.querySelector('[name="dog"]').value = meal.dog_id;
  form.querySelector('[name="food"]').value = meal.food_id;
  form.querySelector('[name="meal"]').value = meal.meal;
  form.querySelector('[name="amount"]').value = meal.amount;
  form.querySelector('[name="date"]').value = meal.date.slice(0, 16);
}

export async function handleDeleteMeal(mealId) {
  if (!confirm("Are you sure you want to delete this meal?")) return;

  try {
    const res = await fetch(`/meals/${mealId}/delete/`, {
      method: "POST",
    });

    if (!res.ok) throw new Error("Failed to delete meal");

    const row = document.querySelector(`#meal-row-${mealId}`);
    if (row) row.remove();

  } catch (err) {
    alert(err.message);
    console.error(err);
  }
}
