# Django Learning Projects

This repository contains Django learning projects including a tutorial application and a first project with restaurant functionality.

## Projects Overview

### 1. Django Tutorial (`djangotutorial/`)
A polls application following the Django official tutorial, featuring:
- Question and Choice models for creating polls
- Admin interface for managing questions and choices
- Public interface for voting and viewing results
- Template system for rendering poll pages

#### Features:
- **Models**: Question and Choice models with relationships
- **Views**: Index, detail, and results views
- **Templates**: HTML templates for poll display
- **Admin**: Django admin interface integration
- **Database**: SQLite database with migrations

### 2. First Project (`firstproject/`)
A restaurant reservation system with:
- Menu item management
- Reservation system with customer details
- Form handling for reservations

#### Features:
- **Models**: MenuItem and Reservation models
- **Forms**: Custom forms for user input
- **Templates**: HTML templates for the restaurant interface
- **Database**: SQLite database with migrations

## Project Structure

```
├── Pipfile                     # Python dependencies
├── djangotutorial/            # Tutorial project
│   ├── db.sqlite3            # Database file
│   ├── manage.py             # Django management script
│   ├── mysite/               # Main project settings
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py       # Project settings
│   │   ├── urls.py           # URL configuration
│   │   └── wsgi.py
│   └── polls/                # Polls application
│       ├── admin.py          # Admin configuration
│       ├── apps.py           # App configuration
│       ├── models.py         # Data models
│       ├── tests.py          # Tests
│       ├── urls.py           # URL patterns
│       ├── views.py          # View functions
│       ├── migrations/       # Database migrations
│       └── templates/        # HTML templates
│           └── polls/
│               ├── detail.html
│               ├── index.html
│               └── results.html
└── firstproject/             # Restaurant project
    ├── db.sqlite3            # Database file
    ├── manage.py             # Django management script
    ├── firstproject/         # Main project settings
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py       # Project settings
    │   ├── urls.py           # URL configuration
    │   └── wsgi.py
    └── fistapp/              # Restaurant application
        ├── admin.py          # Admin configuration
        ├── apps.py           # App configuration
        ├── forms.py          # Form definitions
        ├── models.py         # Data models
        ├── tests.py          # Tests
        ├── urls.py           # URL patterns
        ├── views.py          # View functions
        ├── migrations/       # Database migrations
        └── templates/        # HTML templates
            └── index.html
```

## Requirements

- Python 3.9+
- Django (latest version)
- Pipenv for dependency management

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/darkomike/DJANGO.git
   cd DJANGO
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **For Django Tutorial Project:**
   ```bash
   cd djangotutorial
   python manage.py migrate
   python manage.py createsuperuser  # Optional: create admin user
   python manage.py runserver
   ```
   Access at: http://127.0.0.1:8000/polls/

4. **For First Project:**
   ```bash
   cd firstproject
   python manage.py migrate
   python manage.py createsuperuser  # Optional: create admin user
   python manage.py runserver
   ```
   Access at: http://127.0.0.1:8000/

## Key Learning Concepts

### Django Tutorial Project
- **Models**: Defining database schema with Django ORM
- **Views**: Processing requests and returning responses
- **Templates**: Rendering HTML with Django template language
- **URLs**: URL routing and pattern matching
- **Admin**: Using Django's built-in admin interface
- **Forms**: Handling user input and form validation

### First Project
- **Restaurant Management**: Menu items and pricing
- **Reservations**: Customer reservation system
- **Forms**: Custom form creation and handling
- **Model Relationships**: Foreign keys and data relationships

## Database Models

### Django Tutorial - Polls App
- **Question**: Contains question text and publication date
- **Choice**: Contains choice text, votes count, and foreign key to Question

### First Project - Restaurant App
- **MenuItem**: Contains name and price for menu items
- **Reservation**: Contains customer details and reservation information

## Running Tests

```bash
# For Django Tutorial
cd djangotutorial
python manage.py test polls

# For First Project
cd firstproject
python manage.py test fistapp
```

## Contributing

This is a learning repository. Feel free to fork and experiment with the code.

## License

This project is for educational purposes.

## Notes

- Both projects use SQLite as the database for simplicity
- Database files (`db.sqlite3`) are included for immediate testing
- Admin interfaces are available for both projects
- Templates are included for basic UI functionality

## Next Steps

- Add more advanced features like user authentication
- Implement REST APIs using Django REST Framework
- Add CSS styling and responsive design
- Deploy to a cloud platform like Heroku or AWS