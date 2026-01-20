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

export async function show_dogs(dogs, page) {
  if(page){
    setPage(page, "My Dogs");
  }

  const addBtn = createButton("Add Dog +", async () => {
    form.style.display = form.style.display === "none" ? "block" : "none";
  });

  const form = await createAddDogForm();

  page.dashboard.append(addBtn, form);

  if (dogs && dogs.length) {
    const template = document.getElementById("dog-card-template");
    const cardDeck = document.createElement("div");
    cardDeck.className = "card-deck";

    dogs.forEach(dog => {
      const clone = template.content.cloneNode(true);

      clone.querySelector(".dog-link").href = `/dogs/${dog.id}`;
      clone.querySelector(".dog-image").src = dog.image;
      clone.querySelector(".dog-name").textContent = dog.name;
      clone.querySelector(".dog-breed").textContent = dog.breed_name;
      clone.querySelector(".dog-gender").textContent = dog.gender;
      clone.querySelector(".dog-age").textContent = dog.age;

      cardDeck.appendChild(clone);
    });

    page.dashboard.appendChild(cardDeck);
  } else {
    const p = document.createElement("p");
    p.textContent = "No dogs yet.";
    page.dashboard.appendChild(p);
  }
}


export async function createAddDogForm() {
  const form = document.createElement("form");
  form.id = "add-dog";
  form.style.display = "none";
  form.className = "mb-4";

  // Name
  form.appendChild(createInput("name", "text", "Dog Name"));

  // Image
  form.appendChild(createInput("image", "url", "Image URL"));

  // Gender
  form.appendChild(createSelect("gender", "Gender", ["male", "female"]));

  // Age
  form.appendChild(createInput("age", "number", "Age"));

  // Breed
  const breedDiv = createSelect("breed", "Breed", []);
  form.appendChild(breedDiv);
  const breedSelect = breedDiv.querySelector("select");

  try {
    const res = await fetch("/breeds");
    const breeds = await res.json();

    breeds.forEach(b => {
      const option = document.createElement("option");
      option.value = b.id;
      option.textContent = b.name;
      breedSelect.appendChild(option);
    });
  } catch {
    const option = document.createElement("option");
    option.textContent = "Failed to load breeds";
    option.disabled = true;
    breedSelect.appendChild(option);
  }

  const submit = document.createElement("button");
  submit.type = "submit";
  submit.className = "btn btn-success mt-3";
  submit.textContent = "Add Dog";

  form.appendChild(submit);
  form.addEventListener("submit", handleDogSubmit);

  return form;
}

export async function handleDogSubmit(e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  try {
    const res = await fetch("/dog", {
      method: "POST",
      body: formData,
    });

    if (!res.ok) throw new Error("Failed to add dog");

    const dog = await res.json();

    // Create new card from template
    const template = document.getElementById("dog-card-template");
    const clone = template.content.cloneNode(true);

    clone.querySelector(".dog-link").href = `/dogs/${dog.id}/`;
    clone.querySelector(".dog-image").src = dog.image;
    clone.querySelector(".dog-name").textContent = dog.name;
    clone.querySelector(".dog-breed").textContent = dog.breed_name;
    clone.querySelector(".dog-gender").textContent = dog.gender;
    clone.querySelector(".dog-age").textContent = dog.age;


    if(document.querySelector(".card-deck")){
      const cardDeck = document.createElement("div");
      cardDeck.className = "card-deck";
      document.querySelector(".dog-dashboard").appendChild(cardDeck);
    }
    document.querySelector(".card-deck").appendChild(clone);


    form.reset();
    form.style.display = "none";

  } catch (err) {
    alert(err.message);
  }
}
