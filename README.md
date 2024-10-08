# Expense Tracker

This is a simple command-line based Expense Tracker built in Python. It allows users to add expenses, view them, and generate summaries by month and category. The data is stored in a JSON file so that it persists between sessions.

## Features
- Add an expense with a description, category, and amount.
- View all expenses with date, category, amount, and description.
- Get a monthly summary of expenses.
- Get a category-wise summary of expenses.
- Data is saved to a `JSON` file (`expenses.json`) for persistence.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <>
    ```

2. **Navigate to the project directory**:
    ```bash
    cd expense-tracker
    ```

3. **Run the script**:
    Ensure that you have Python 3.x installed. You can run the application directly using:
    ```bash
    python expense_tracker.py
    ```

## Usage

1. When you run the script, you will see a menu with the following options:
    ```
    1. Add Expense
    2. View Expenses
    3. Monthly Summary
    4. Category Summary
    5. Exit
    ```

2. **Add Expense**:
    - Enter the amount, description, and category for the expense. 
    - The data will be saved and persisted in `expenses.json`.

3. **View Expenses**:
    - Lists all the expenses with the amount, description, category, and date.

4. **Monthly Summary**:
    - Displays the total expenses for each month.

5. **Category Summary**:
    - Displays the total expenses for each category.

6. **Exit**:
    - Exits the application.

## File Structure

