import {show_meals} from '../profile/meals.js';
import {show_activities} from '../profile/activities.js';
import {show_craps} from '../profile/craps.js';

document.addEventListener('DOMContentLoaded', function() {
    // area to fill
    const page = {
      title: document.querySelector('h3.display-6'),
      dashboard: document.querySelector('.dog-dashboard')
    };

    // get JSON data
    const dog = [JSON.parse(document.getElementById("dog-data").textContent)];
    const meals = JSON.parse(document.getElementById("meals-data").textContent);
    const activities = JSON.parse(document.getElementById("activities-data").textContent);
    const craps = JSON.parse(document.getElementById("craps-data").textContent);

    // add event listeners to buttons
    document.querySelector('#dog-meals-btn').addEventListener('click', () => show_meals(meals, page, dog));
    document.querySelector('#dog-activity-btn').addEventListener('click', ()=> show_activities(activities, page, dog));
    document.querySelector('#dog-crap-btn').addEventListener('click', () => show_craps(craps, page, dog));
});
