class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
    
    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"

    def to_dict(self):
        return {
            'Date': self.date,
            'Category': self.category,
            'Amount': self.amount,
            'Description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data['Amount'],
            category=data['Category'],
            date=data['Date'],
            description=data['Description']
        )
