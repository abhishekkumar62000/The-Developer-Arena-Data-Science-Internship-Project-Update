# Month 1: Python Programming Mastery - Personal Finance Manager

A comprehensive personal finance management system with object-oriented design, file handling, data persistence, and a user-friendly command-line interface to track expenses, generate reports, and analyze spending patterns.

## 🎯 Features
- **Object-Oriented Design**: Utilizes an `Expense` class to manage financial objects.
- **Data Persistence**: Uses a CSV module for reading/writing logic inside the `data/` directory.
- **Robust Error Handling**: Validates user input (float conversions, Date parsing, specific Categories filter).
- **Interactive CLI**: Menu-based terminal application to manage inputs.
- **Analysis and Reports**: Generate monthly reports and category-wise summaries for clear tracking.
- **Data Backup**: Create instant backups of your expense.csv.

## 📁 Project Structure
```
Personal Finance Manager/
├── main.py             # Main program entry point
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── src/                # Source code modules
│   ├── expense.py      # Expense class definition
│   ├── utils.py        # Utility/validation functions
│   ├── file_manager.py # CSV read/write and backup operations
│   ├── reports.py      # Summary and report generation logic
│   └── menu.py         # CLI logic
├── data/               # Contains CSV files and backups
├── reports/            # Output folder for generated text reports
├── docs/               # Documentation
├── tests/              # Unit tests
└── screenshots/        # Application screenshots
```

## 🛠️ Setup Instructions
1. Ensure you have Python 3.7+ installed.
2. Clone this repository or download the package.
3. Open a terminal in the project root directory (`Personal Finance Manager`).
4. (Optional) Run `pip install -r requirements.txt` (currently no external dependencies).
5. Run the application via `python main.py`.

## 🚀 Usage Guide
1. **Add New Expense**: Start tracking your spending by entering an amount, pre-defined category, date (YYYY-MM-DD), and description.
2. **View All Expenses**: Lists all current records sorted by date.
3. **Category-wise Summary**: Prints a clear table outlining what percentage of your total went to which category.
4. **Generate Monthly Report**: Groups expenses by Month/Year format (e.g., 2024-01) for overall trends.
5. **Search**: Find specific spending using keyword searches in description/date.
6. **Backup Data**: Safely duplicate your current `.csv` so no progress is lost.

Enjoy tracking your expenses!
