# ExTrack (Expense Tracker)

ExTrack is a premium, mobile-first, Django-based web application to help you keep track of your expenses flawlessly. Built with a sleek Midnight Dark Glassmorphism interface, it allows for secure multi-user management, rich charting analytics, and easy tracking of individual expenses.

## ✨ Features

- **Premium UI/UX:** Responsive mobile-first design with interactive elements, off-canvas navigation menus, and Glassmorphism styling.
- **Secure Authentication:** Multi-user support so everyone's data remains completely private and perfectly organized.
- **Comprehensive Expense Management:** Add new expenses with designated Names, predefined Categories, and Amounts.
- **Analytics Dashboard:** Visual representation of your spending habits using Chart.js (Doughnut category breakdown and historical Line charts).
- **Advanced Filtering:** Stacked, mobile-friendly forms to filter your entire expense history by Category, specific Date Ranges, and Amount boundaries.
- **Swipeable Data Tables:** Horizontally scrollable data tables explicitly built for mobile constraints.

## 🚀 Technologies Used

- **Framework:** Django 3.2.12
- **Language:** Python 3.12 
- **Database:** Neon Serverless PostgreSQL (Production) / SQLite (Local)
- **Frontend:** Vanilla HTML5, modern CSS3 (Flexbox/Grid), secure Vanilla JS, Chart.js
- **Deployment & Hosting:** Vercel (Serverless Edge Python Runtime), WhiteNoise (for static file caching)

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.10+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sujeetmadihalli/ExpenseTracker.git
   cd ExpenseTracker
   ```

2. **Activate a Python Environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Setup the Database:**
   *(By default, this runs locally on SQLite if no DATABASE_URL is provided)*
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📂 Project Structure
*(Simplified)*
```text
ExpenseTracker/
├── expense_tracker/  # Core Django config, URL routing, settings
├── expenses/         # Main business logic, models, views, and templates
│   ├── static/       # CSS and JS assets (styles.css, scripts.js)
│   ├── templates/    # UI definitions (base.html, dashboard.html, etc.)
├── build_files.sh    # Vercel deployment hook
├── vercel.json       # Vercel serverless routing configuration
└── requirements.txt  # Python package dependencies
```

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.
