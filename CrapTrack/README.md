# CrapTrack

## Overview

CrapTrack is a web application built with Django and JavaScript that allows dog owners to log and review information about their dogs’ meals, daily activities, and bowel movements. The application provides a centralized dashboard where users can view and manage time-based data related to their dogs’ health and habits.

## Distinctiveness and Complexity

### Distinctiveness

CrapTrack is clearly distinct from the projects previously completed in CS50 Web Programming with Python and JavaScript. The app is not a social network. It does not include user-generated posts, follows, likes, or messaging features. The app is not an e-commerce site. There are no products for sale, no bidding, no likes, and no listings.

Unlike earlier course projects, CrapTrack is a personal data tracking app focused on health-related records for pets. The core functionality centers on logging and analyzing structured, time-based data across multiple related categories (meals, activities, craps) for multiple dogs, which is not addressed by any prior CS50W project.

### Complexity

The project demonstrates substantial complexity in both backend and frontend design.

- Multiple Django models with relational structure, including:
    - Dogs and Ownership relationships
    - Meals, Activities, and Crap records linked to both users and dogs
    - Many-to-many relationship between ingredients and recipes
- Use of Django’s ORM for filtering, annotating, and enforcing user-specific data access
- REST-like endpoints returning JSON data consumed by the frontend
- A JavaScript-driven interface that:
    - Dynamically generates forms and tables
    - Fetches and renders data asynchronously
    - Updates the UI without full page reloads
- Clear separation of concerns between:
    - Django views (data validation and persistence)
    - JavaScript helper utilities
    - HTML templates
- Mobile responsiveness implemented using Bootstrap

Overall, the application exceeds the complexity of earlier coursework and integrates multiple technologies in a cohesive way.

## File Structure and Contents

### Root Directory
manage.py

### Application: dog
- Backend (Python / Django)
    - models.py
        - Defines all database models, including Dog, Ownership, Meal, Activity, Crap, Breed, Food, and Brand.
    - views.py
    - urls.py

### Templates

- layout.html ~ Base layout template used across pages.
- profile.html ~ Main user dashboard template. Content is populated dynamically using JavaScript.
- dog.html ~ Displays all meals, activities, and craps for a single dog.
- dogCard.html ~ Creates a componet like template, cloned in Javascript to allow multiple uses

## How to Run the Application

1. Clone the repository and navigate to the project directory:
`git clone <repo url>`
`cd CrapTrack`

2. Create and activate a virtual environment:
`python -m venv venv`
`source venv/bin/activate      # macOS / Linux`
`venv\Scripts\activate         # Windows`

3. Install dependencies:
`pip install django`

4. Apply database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

5. Run the development server:
`python manage.py runserver`

## Additional Information

- All application data is scoped to the authenticated user. Users may only view and modify records associated with their own account.
- Data is submitted and retrieved using asynchronous JavaScript requests rather than full page reloads.
- Edit and delete functionality was intentionally excluded to maintain a clear focus on core tracking and data visualization features.
- The project was designed to be extensible, allowing for future enhancements such as trend analysis or data visualization without restructuring the existing system.

## Future Work

While CrapTrack currently focuses on structured data collection and visualization, the application was designed with extensibility in mind. Several potential enhancements could further expand its analytical and practical value.
One planned area of expansion is a trends and correlation feature. By analyzing historical meal, activity, and bowel movement data for individual dogs, the application could identify patterns and correlations, such as relationships between specific foods and changes in bowel consistency, frequency, or volume. This would allow users to make more informed decisions about diet and routine adjustments.
Another area for future development is support for additional pet types, such as cats or other small animals. While the current data models are tailored to dogs, the underlying structure could be generalized to support multiple species, each with customizable tracking categories. This would broaden the application’s usefulness and allow multi-pet households to manage all pet health data within a single platform.
Additional improvements could include data visualization dashboards and exportable reports for veterinary visits. These enhancements could be layered onto the existing architecture without major changes to the core system.
