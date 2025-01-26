# E-commerce Inventory Management System

A Django and React-based inventory management system for e-commerce stores, designed to streamline product management, categorization, and inventory tracking. The system features a user-friendly interface and a comprehensive test suite to ensure reliability.

## Key Features

- **Product Management**: Supports CRUD operations for efficient product lifecycle management.
- **Category Management**: Enables categorization of products for easy organization and filtering.
- **Inventory Tracking**: Real-time monitoring of product quantities to prevent stockouts and overstocking.
- **Modern UI**: React-based frontend for a responsive and intuitive user experience.
- **Comprehensive Test Suite**: Ensures the system's reliability through extensive testing.

## Prerequisites

- **Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Node.js**: Ensure Node.js version 14.x or higher is installed on your system to run React 19. You can download it from [nodejs.org](https://nodejs.org/).

## Setup Instructions

1. **Virtual Environment Setup**: Create and activate a virtual environment to isolate project dependencies.
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
2. **Install Dependencies**: Go to the local repository directory. Install the required dependencies listed in `requirements.txt` using pip.
   ```bash
   pip install -r requirements.txt
   ```
3. **Database Setup**: (Optional) Configure the database settings in `settings.py` according to your database management system.

4. **Create and Run Migrations**: Execute `python manage.py migrate` to apply database migrations.
   ```bash
   cd ecommerce_inventory
   python manage.py migrate
   ```
5. **Start the Server**: Launch the development server using `python manage.py runserver`.
   ```bash
   python manage.py runserver
   ```
6. **React Frontend Setup**: Navigate to the frontend directory and install the required dependencies.
   ```bash
   cd ../frontend
   npm install
   ```
7. **Start the React Development Server**: Launch the React development server.
   ```bash
   npm start
   ```
8. **Navigate to the React App**: Open your web browser and go to `http://localhost:3000` to access the application.
   ```plaintext
   http://localhost:3000
   ```

## Project Structure

```
project_root/
├── ecommerce_inventory/ # Backend Django project
│ ├── inventory/ # Main app for inventory management
│ │ ├── migrations/ # Database migrations
│ │ ├── init.py # Package marker
│ │ ├── admin.py # Admin interface configuration
│ │ ├── apps.py # App configuration
│ │ ├── models.py # Database models
│ │ ├── tests.py # Test cases
│ │ ├── views.py # Views for handling requests
│ │ └── services.py # Business logic and services
│ │
│ ├── ecommerce_inventory/ # Project settings
│ │ ├── init.py # Package marker
│ │ ├── settings.py # Project settings
│ │ ├── urls.py # URL routing
│ │ └── wsgi.py # WSGI application
│ │
│ └── manage.py # Django command-line utility
│
├── frontend/ # React frontend application
│ ├── public/ # Static files
│ ├── src/ # Source code
│ │ ├── components/ # React components
│ │ │ ├── CategoryForm.js # Category creation form
│ │ │ ├── CategoryList.js # Category listing
│ │ │ ├── ProductForm.js # Product creation form
│ │ │ ├── ProductList.js # Product listing
│ │ │ ├── ProductUpdateModal.js # Product update modal
│ │ │ ├── ProductManagement.js # Product management wrapper
│ │ │ └── InventoryManagement.js# Main inventory component
│ │ ├── services/ # API services
│ │ │ └── api.js # API integration
│ │ ├── App.js # Root component
│ │ └── index.js # Entry point
│ │
│ ├── package.json # NPM dependencies
│ └── README.md # Frontend documentation
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation              # Project documentation
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
