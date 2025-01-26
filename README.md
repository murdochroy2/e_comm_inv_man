# E-commerce Inventory Management System

A Django-based inventory management system for e-commerce stores, designed to streamline product management, categorization, and inventory tracking. The system features a user-friendly admin interface and a comprehensive test suite to ensure reliability.

## Key Features

- **Product Management**: Supports CRUD (Create, Read, Update, Delete) operations for efficient product lifecycle management.
- **Category Management**: Enables categorization of products for easy organization and filtering.
- **Inventory Tracking**: Real-time monitoring of product quantities to prevent stockouts and overstocking.
- **Admin Interface**: Intuitive interface for administrators to manage the system effectively.
- **Comprehensive Test Suite**: Ensures the system's reliability and stability through extensive testing.

## Setup Instructions

1. **Virtual Environment Setup**: Create and activate a virtual environment to isolate project dependencies.
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
2. **Install Dependencies**: Install the required dependencies listed in `requirements.txt` using pip.
   ```bash
   pip install -r requirements.txt
   ```
3. **Database Setup**: Configure the database settings in `settings.py` according to your database management system.

4. **Create and Run Migrations**: First, create migrations for the "inventory" app using `python manage.py makemigrations inventory`. Then, execute `python manage.py migrate` to apply database migrations.
   ```bash
   python manage.py makemigrations inventory
   python manage.py migrate
   ```
5. **Start the Server**: Launch the development server using `python manage.py runserver`.
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
ecommerce_inventory/
    ├── inventory/                # Main app for inventory management
    │   ├── migrations/           # Database migrations
    │   ├── __init__.py           # Package marker
    │   ├── admin.py              # Admin interface configuration
    │   ├── apps.py               # App configuration
    │   ├── models.py             # Database models
    │   ├── tests.py              # Test cases
    │   ├── views.py              # Views for handling requests
    │   └── services.py           # Business logic and services
    │
    ├── ecommerce_inventory/       # Project settings
    │   ├── __init__.py           # Package marker
    │   ├── settings.py            # Project settings
    │   ├── urls.py                # URL routing
    │   └── wsgi.py                # WSGI application
    │
    ├── manage.py                  # Command-line utility for administrative tasks
    ├── requirements.txt           # Project dependencies
    └── README.md                  # Project documentation
```

## Decision Log

- **Django Framework**: Chosen for its robustness, scalability, and extensive libraries.
- **Database**: Supports various database management systems, including MySQL, PostgreSQL, and SQLite.
- **Testing Framework**: Utilizes pytest and pytest-django for comprehensive unit testing and integration testing.

## Testing Strategy

- **Unit Testing**: Focuses on individual components, such as models, views, and forms, to ensure they function as expected.
- **Integration Testing**: Verifies the interaction between components, including API endpoints and user interface interactions.
- **Test Coverage**: Aims to achieve high test coverage to ensure the system's reliability and stability.

## Testing Commands

To run the tests for the project, follow these commands:

1. **Run All Tests**: Execute all tests using pytest.
   ```bash
   pytest
   ```
