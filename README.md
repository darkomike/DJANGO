# Django Learning Journey

This repository documents my Django learning path as I build skills for web development projects and career opportunities. It contains hands-on projects that demonstrate progressively advanced Django concepts and real-world development patterns.

## Learning Objectives & Skills Development

Through these projects, I'm developing key competencies required for modern web development roles:

### 1. Django Tutorial (`djangotutorial/`) - **Foundation Skills**
My first step into Django development, building a polls application to master core concepts:
- **Learning Focus**: Understanding Django's MVC pattern and basic web development workflows
- **Skills Acquired**: Model design, view logic, template rendering, and admin interface usage
- **Industry Relevance**: These are essential skills for any Django developer position

**Key Features Implemented:**
- Question and Choice models with proper relationships
- Admin interface for content management
- Public-facing voting interface
- URL routing and view handling

### 2. First Project (`firstproject/`) - **Business Application Skills**
A restaurant reservation system that demonstrates real-world business logic implementation:
- **Learning Focus**: Building applications that solve actual business problems
- **Skills Acquired**: Form handling, data validation, and user input processing
- **Industry Relevance**: Restaurant/hospitality sector applications are common in freelance and enterprise work

**Key Features Implemented:**
- Menu item management system
- Customer reservation handling with validation
- Custom forms for user interaction
- Database relationships for business data

### 3. Django REST Framework Tutorial (`rest_tutorial/`) - **Modern API Development**
A code snippet sharing API that builds essential backend development skills:
- **Learning Focus**: RESTful API design and implementation using industry-standard tools and production-level patterns
- **Skills Acquired**: API serialization, authentication, permissions, user management, automated processing, and production-ready architecture
- **Industry Relevance**: REST APIs with authentication and user management are fundamental in modern web applications

**Key Features Implemented:**
- User authentication and authorization system with Django's built-in User model
- Permission-based access control (IsAuthenticatedOrReadOnly)
- Automatic syntax highlighting with custom model save() method using Pygments
- User management API endpoints for complete user operations
- Owner-based snippet association and read-only serialization
- Django REST Framework authentication integration (api-auth/)
- Advanced model relationships and serializer configurations
- Production-ready API with security, user management, and automated processing

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
└── rest_tutorial/            # Django REST Framework tutorial
    ├── db.sqlite3            # Database file
    ├── manage.py             # Django management script
    ├── rest_tutorial/        # Main project settings
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py       # Project settings
    │   ├── urls.py           # URL configuration
    │   └── wsgi.py
    └── snippets/             # Code snippets API app
        ├── admin.py          # Admin configuration
        ├── apps.py           # App configuration
        ├── models.py         # Snippet model
        ├── serializers.py    # REST serializers
        ├── tests.py          # Tests
        ├── urls.py           # API URL patterns
        ├── views.py          # API view functions
        └── migrations/       # Database migrations
```

## Technical Stack & Professional Tools

**Core Technologies I'm Mastering:**
- Python 3.9+
- Django (latest version)
- Django REST Framework
- Pygments (for syntax highlighting)
- SQLite database management
- Pipenv for dependency management

These tools represent industry standards that I'm learning to prepare for professional development roles.

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

5. **For Django REST Framework Tutorial:**
   ```bash
   cd rest_tutorial
   python manage.py migrate
   python manage.py runserver
   ```
   Access API at: http://127.0.0.1:8000/snippets/
   
   You can test the API using tools like HTTPie or curl:
   ```bash
   pip install httpie
   http GET http://127.0.0.1:8000/snippets/
   ```

## Skills Acquired & Professional Development

### Django Tutorial Project - **Foundation Building**
- **Models**: Learning database schema design with Django ORM - essential for backend roles
- **Views**: Understanding request/response cycles - core web development concept
- **Templates**: HTML rendering with Django template language - full-stack development skill
- **URLs**: Mastering URL routing patterns - fundamental web architecture knowledge
- **Admin**: Leveraging Django's admin interface - valuable for rapid prototyping in startups
- **Forms**: Building user input handling - critical for interactive web applications

### First Project - **Business Logic Implementation**
- **Restaurant Management**: Applying Django skills to real-world business scenarios
- **Reservations**: Building customer-facing features that solve actual problems
- **Forms**: Advanced form creation and validation - essential for data-driven applications
- **Model Relationships**: Understanding foreign keys and data relationships - database design expertise

### Django REST Framework Tutorial - **Modern Backend Development**
- **REST APIs**: Building APIs that power modern web and mobile applications
- **Authentication & Authorization**: Implementing secure user-based access control with Django's permission system
- **User Management**: Creating complete user API endpoints for user registration and management
- **Advanced Model Logic**: Custom save methods for automated processing (syntax highlighting)
- **Permissions System**: Using IsAuthenticatedOrReadOnly for secure read/write access patterns
- **Serializer Relationships**: Managing complex data relationships between users and content
- **Security Integration**: Django REST Framework authentication with browsable API security
- **Production Features**: Building APIs with authentication, permissions, and automated processing ready for deployment

## Project Portfolio & Technical Showcase

### Django Tutorial - Polls App **[Foundation Skills Demo]**
- **Question**: Demonstrates one-to-many relationships and timestamp handling
- **Choice**: Shows foreign key implementation and vote counting logic

### First Project - Restaurant App **[Business Application Demo]**
- **MenuItem**: Displays basic CRUD operations for business inventory
- **Reservation**: Implements complex business logic with customer data validation

### Django REST Framework Tutorial - Snippets App **[API Development Demo]**
- **Snippet**: Showcases advanced model design with automated processing capabilities
  - `created`: Auto-timestamp implementation
  - `title`: Optional field handling
  - `code`: Large text storage for content
  - `linenos`: Boolean logic for UI preferences
  - `language`: Choice field with dynamic options
  - `style`: Integration with third-party library choices
  - `owner`: Foreign key relationship to User model for ownership tracking
  - `highlighted`: Auto-generated HTML syntax highlighting using custom save() method

- **User**: Demonstrates user management and relationship modeling
  - User API endpoints for complete user management
  - Related snippets through foreign key relationships
  - Authentication and permission integration

This demonstrates advanced Django model relationships, custom processing, and production-ready API architecture.

## Testing & Quality Assurance Skills

Learning proper testing practices to ensure code reliability and maintainability:

```bash
# Django Tutorial - Testing foundation concepts
cd djangotutorial
python manage.py test polls

# First Project - Business logic testing
cd firstproject
python manage.py test fistapp

# Django REST Framework - API endpoint testing
cd rest_tutorial
python manage.py test snippets
```

## Career Development Goals

This learning repository demonstrates my commitment to building production-ready skills:

- **Current Focus**: Mastering Django fundamentals and REST API development
- **Portfolio Building**: Each project showcases different aspects of web development
- **Industry Standards**: Learning tools and patterns used in professional environments
- **Problem Solving**: Applying technical skills to solve real-world business challenges
- **Code Quality**: Implementing testing and following best practices

## Development Environment & Best Practices

**What I'm Learning:**
- All projects use SQLite for rapid development and learning
- Database files included for immediate testing and demonstration
- Admin interfaces showcase Django's built-in tools for content management
- Templates demonstrate full-stack development capabilities
- REST API provides backend skills essential for modern development roles
- Testing implementation shows commitment to code quality

## Next Steps in My Learning Journey

**Immediate Goals:**
- Add user authentication and authorization systems
- Implement advanced REST API features like pagination and filtering
- Learn frontend integration with modern JavaScript frameworks
- Deploy applications to cloud platforms for portfolio demonstration

**Career Objectives:**
- Build a portfolio that demonstrates full-stack capabilities
- Develop skills applicable to startup and enterprise environments
- Master modern web development patterns and industry best practices
- Prepare for technical interviews and practical coding assessments