# Flask MVC Blog Engine

A lightweight Content Management System (CMS) built with Python and Flask, architected using the Model-View-Controller (MVC) pattern. 

The goal of this project was to refactor a monolithic script into a scalable, modular blog application. It features a complete separation of concerns between data logic (Models), routing (Controllers), and user interface (Views).

## Key Features

### Architecture & Backend
* **MVC Pattern:** Strict separation of logic.
    * **Models:** SQLite database interactions handled via `app/models.py`.
    * **Controllers:** HTTP routing and business logic in `app/routes.py` using Flask Blueprints.
    * **Views:** Dynamic HTML rendering in `app/templates/`.
* **Authentication:** Custom session-based authentication system with password hashing (`werkzeug.security`).
* **Database:** Relational data modeling with SQLite using parameterized queries to prevent SQL injection.

### Frontend
* **Jinja2 Templating:** Utilizes template inheritance (`base.html`) to enforce DRY (Don't Repeat Yourself) principles across the UI.
* **Interactive UI:** Includes CSS animations, responsive cards, and dynamic JavaScript effects for user interaction.

