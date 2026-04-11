import csv
import os
import shutil
from datetime import datetime
from src.expense import Expense

DEFAULT_DATA_FILE = os.path.join('data', 'expenses.csv')
DEFAULT_BACKUP_DIR = 'data'

def load_expenses(filename=DEFAULT_DATA_FILE):
    expenses = []
    if not os.path.exists(filename):
        return expenses
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    exp = Expense.from_dict(row)
                    expenses.append(exp)
                except Exception as e:
                    print(f"Skipping malformed row: {row} - {e}")
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        
    return expenses

def save_expenses(expenses, filename=DEFAULT_DATA_FILE):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Date', 'Category', 'Amount', 'Description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
        return True
    except Exception as e:
        print(f"Error saving to file {filename}: {e}")
        return False

def backup_data(filename=DEFAULT_DATA_FILE, backup_dir=DEFAULT_BACKUP_DIR):
    if not os.path.exists(filename):
        print("No data file found to backup.")
        return False
        
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f'expenses_backup_{timestamp}.csv')
    
    try:
        shutil.copy2(filename, backup_file)
        print(f"Backup created successfully: {backup_file}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False
