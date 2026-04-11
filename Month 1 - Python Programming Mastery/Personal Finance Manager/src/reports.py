import os
from collections import defaultdict
from itertools import groupby

def generate_monthly_report(expenses):
    print("\n--- MONTHLY REPORT ---")
    if not expenses:
        print("No expenses found.")
        return
        
    expenses.sort(key=lambda x: x.date)
    monthly_data = defaultdict(float)
    
    for expense in expenses:
        month_yr = expense.date[:7] # YYYY-MM
        monthly_data[month_yr] += expense.amount
        
    for month, total in monthly_data.items():
        print(f"Month: {month} - Total Spent: ₹{total:.2f}")

def view_category_summary(expenses):
    print("\n--- CATEGORY-WISE SUMMARY ---")
    if not expenses:
        print("No expenses found.")
        return
        
    summary = defaultdict(float)
    total_spent = 0
    
    for expense in expenses:
        summary[expense.category] += expense.amount
        total_spent += expense.amount
        
    print(f"{'Category':<15} | {'Total spent (₹)':<15} | {'% of Total':<10}")
    print("-" * 50)
    for category, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total_spent) * 100 if total_spent > 0 else 0
        print(f"{category:<15} | ₹{amount:<14.2f} | {percentage:.1f}%")
    print("-" * 50)
    print(f"{'TOTAL':<15} | ₹{total_spent:<14.2f} | 100.0%\n")

def __save_report_to_file(title, content):
    os.makedirs('reports', exist_ok=True)
    filename = os.path.join('reports', f"{title.replace(' ', '_').lower()}.txt")
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Failed to write report to file: {e}")
