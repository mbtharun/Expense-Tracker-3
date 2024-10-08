import json  
from datetime import datetime  

class ExpenseTracker:  
    def __init__(self):  
        self.expenses = []  
        self.load_data()  

    def load_data(self):  
        try:  
            with open('expenses.json', 'r') as file:  
                self.expenses = json.load(file)  
        except (FileNotFoundError, json.JSONDecodeError):  # Handles both missing file and decoding issues
            self.expenses = []  

    def save_data(self):  
        with open('expenses.json', 'w') as file:  
            json.dump(self.expenses, file, indent=4)  # Adding indent for better readability

    def add_expense(self, amount, description, category):  
        expense = {  
            'amount': float(amount),  # Ensuring amount is stored as float
            'description': description,  
            'category': category,  
            'date': datetime.now().strftime("%Y-%m-%d")  
        }  
        self.expenses.append(expense)  
        self.save_data()  
        print("Expense added successfully!")  

    def view_expenses(self):  
        if not self.expenses:  
            print("No expenses recorded.")  
            return  
        for expense in self.expenses:  
            print(f"{expense['date']} - {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")  

    def monthly_summary(self):  
        summary = {}  
        for expense in self.expenses:  
            month = expense['date'][:7]  # Get the year-month  
            if month not in summary:  
                summary[month] = 0  
            summary[month] += float(expense['amount'])  # Ensure the amount is treated as float
        
        print("Monthly Summary:")  
        for month, total in summary.items():  
            print(f"{month}: ${total:.2f}")  # Display two decimal places for monetary values

    def category_summary(self):  
        summary = {}  
        for expense in self.expenses:  
            category = expense['category']  
            if category not in summary:  
                summary[category] = 0  
            summary[category] += float(expense['amount'])  # Ensure the amount is treated as float
        
        print("Category Summary:")  
        for category, total in summary.items():  
            print(f"{category}: ${total:.2f}")  # Display two decimal places for monetary values

def main():  
    tracker = ExpenseTracker()  
    
    while True:  
        print("\nExpense Tracker")  
        print("1. Add Expense")  
        print("2. View Expenses")  
        print("3. Monthly Summary")  
        print("4. Category Summary")  
        print("5. Exit")  
        
        choice = input("Choose an option: ")  
        
        if choice == '1':  
            try:  
                amount = float(input("Enter amount: "))  
                description = input("Enter description: ")  
                category = input("Enter category: ")  
                tracker.add_expense(amount, description, category)  
            except ValueError:  
                print("Invalid input. Please enter a numeric value for the amount.")  
        
        elif choice == '2':  
            tracker.view_expenses()  
        
        elif choice == '3':  
            tracker.monthly_summary()  
        
        elif choice == '4':  
            tracker.category_summary()  
        
        elif choice == '5':  
            print("Exiting the Expense Tracker. Goodbye!")  
            break  
        
        else:  
            print("Invalid choice. Please select a valid option.")  

if __name__ == "__main__":  
    main()
