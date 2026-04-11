import sys
from datetime import datetime

from src.expense import Expense
from src.utils import validate_amount, validate_category, validate_date, validate_description, VALID_CATEGORIES
from src.file_manager import load_expenses, save_expenses, backup_data
from src.reports import view_category_summary as print_category_summary, generate_monthly_report as print_monthly_report

class FinanceManagerApp:
    def __init__(self):
        self.expenses = load_expenses()

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("\nEnter your choice (1-7): ")
                if choice == '1':
                    self.add_expense()
                elif choice == '2':
                    self.view_all_expenses()
                elif choice == '3':
                    self.view_category_summary()
                elif choice == '4':
                    self.generate_monthly_report()
                elif choice == '5':
                    self.search_expenses()
                elif choice == '6':
                    self.backup_data()
                elif choice == '7':
                    self.exit_app()
                else:
                    print("❌ Invalid choice! Please enter a number between 1 and 7.")
            except Exception as e:
                print(f"❌ An error occurred: {e}")
            input("\nPress Enter to continue...")

    def display_menu(self):
        print("\n" + "="*42)
        print("     PERSONAL FINANCE MANAGER")
        print("="*42)
        print("\nMAIN MENU:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category-wise Summary")
        print("4. Generate Monthly Report")
        print("5. Search Expenses")
        print("6. Backup Data")
        print("7. Exit")

    def add_expense(self):
        print("\nADD NEW EXPENSE:")
        print(f"Categories: {', '.join(VALID_CATEGORIES)}")
        
        while True:
            try:
                amount_str = input("Enter amount: ₹")
                amount = validate_amount(amount_str)
                break
            except ValueError as e: print(f"❌ Error: {e}")

        while True:
            try:
                category_str = input("Enter category: ")
                category = validate_category(category_str)
                break
            except ValueError as e: print(f"❌ Error: {e}")

        while True:
            try:
                date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
                if not date_str:
                    date = datetime.now().strftime("%Y-%m-%d")
                    break
                else:
                    date = validate_date(date_str)
                    break
            except ValueError as e: print(f"❌ Error: {e}")

        while True:
            try:
                desc_str = input("Enter description: ")
                description = validate_description(desc_str)
                break
            except ValueError as e: print(f"❌ Error: {e}")

        # Create expense and save
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        save_expenses(self.expenses)
        print("\n✅ Expense added successfully!")

    def view_all_expenses(self):
        print("\nALL EXPENSES:")
        if not self.expenses:
            print("No expenses recorded yet. Start by adding a new expense.")
            return
            
        # Display sorted by date
        sorted_expenses = sorted(self.expenses, key=lambda x: x.date, reverse=True)
        print('-'*60)
        print(f"{'Date':<15} | {'Category':<15} | {'Amount':<10} | {'Description'}")
        print('-'*60)
        for expense in sorted_expenses:
            print(f"{expense.date:<15} | {expense.category:<15} | ₹{expense.amount:<9.2f} | {expense.description}")
        print('-'*60)
        total = sum(e.amount for e in self.expenses)
        print(f"Total spent across all periods: ₹{total:.2f}")

    def view_category_summary(self):
        print_category_summary(self.expenses)

    def generate_monthly_report(self):
        print_monthly_report(self.expenses)

    def search_expenses(self):
        term = input("Enter search keyword or date (e.g., Grocery, Food, 2024-01): ").lower()
        results = [e for e in self.expenses if term in e.description.lower() or term in e.category.lower() or term in e.date]
        
        if not results:
            print(f"No expenses found matching '{term}'.")
        else:
            print(f"\n🔍 Search Results ({len(results)} found):")
            print('-'*60)
            print(f"{'Date':<15} | {'Category':<15} | {'Amount':<10} | {'Description'}")
            print('-'*60)
            for expense in sorted(results, key=lambda x: x.date, reverse=True):
                print(f"{expense.date:<15} | {expense.category:<15} | ₹{expense.amount:<9.2f} | {expense.description}")
            print('-'*60)

    def backup_data(self):
        backup_data('data/expenses.csv', 'data/')

    def exit_app(self):
        save_expenses(self.expenses)
        print("✅ Data saved. Exiting Personal Finance Manager...")
        sys.exit(0)
