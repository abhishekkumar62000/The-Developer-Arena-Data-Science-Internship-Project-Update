from datetime import datetime

VALID_CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Utility', 'Clothing', 'Medical', 'Other']

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError:
        raise ValueError("Invalid amount. Please enter a positive numerical value.")

def validate_category(category_str):
    category = category_str.title()
    if category not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category. Must be one of: {', '.join(VALID_CATEGORIES)}")
    return category

def validate_date(date_str):
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return valid_date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def validate_description(desc_str):
    if not desc_str or len(desc_str.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    return desc_str.strip()
