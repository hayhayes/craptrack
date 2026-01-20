import {
  createButton,
  createSelect,
  createTable,
  renderRows,
  createInput,
  setPage
} from './helpers.js';

import {show_meals} from './meals.js';
import {show_activities} from './activities.js';
import {show_craps} from './craps.js';
import {show_dogs} from './dogs.js';

document.addEventListener('DOMContentLoaded', function() {

    const page = {
      title: document.querySelector('h3.display-4'),
      dashboard: document.querySelector('.dog-dashboard')
    };

    // get JSON data
    const dogs = JSON.parse(document.getElementById("dogs-data").textContent);
    const meals = JSON.parse(document.getElementById("meals-data").textContent);
    const activities = JSON.parse(document.getElementById("activities-data").textContent);
    const craps = JSON.parse(document.getElementById("craps-data").textContent);

    // use buttons to toggle different views
    document.querySelector('#my-dogs').addEventListener('click', () => show_dogs(dogs, page));
    document.querySelector('#dog-meals').addEventListener('click', () => show_meals(meals, page, dogs));
    document.querySelector('#dog-activity').addEventListener('click', ()=> show_activities(activities, page, dogs));
    document.querySelector('#dog-crap').addEventListener('click', () => show_craps(craps, page, dogs));
    document.querySelector('#dog-trends').addEventListener('click', show_trends);

    // initalize page with my dogs
    show_dogs(dogs, page)

});

function show_trends() {
  setPage("Trends");
  page.dashboard.textContent = "Trends coming soon";
}

