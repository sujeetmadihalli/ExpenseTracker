# Expense Tracker

Expense Tracker is a Django-based web application to help you keep track of your expenses. It allows you to add, list, filter, and delete expense entries.

## Features

- Add new expenses with a category and amount.
- View a list of all expenses.
- Filter expenses by date and category.
- Delete expenses.

## Technologies Used

- Django 3.2.12
- Python 3.10
- SQLite (default database)

## Setup Instructions

### Prerequisites

- Python 3.10
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sujeetmadihalli/ExpenseTracker.git
   cd ExpenseTracker
   
2. Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5.Create a superuser to access the Django admin:

python manage.py createsuperuser

6. Run the development server:

python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000/.

8. Project Structure

expense_tracker/
├── expense_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── expenses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│       ├── expenses/
│           ├── base.html
│           ├── home.html
│           ├── add_expense.html
│           ├── list_expenses.html
│           ├── filter_expenses.html
│           ├── remove_expense.html
├── manage.py
├── requirements.txt

9. Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.







