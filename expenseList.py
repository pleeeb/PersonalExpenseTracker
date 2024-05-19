from datetime import datetime

from expense import Expense


class ExpenseList:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        date = None
        while not date:
            try:
                date = datetime.strptime(input("Please enter the date in the format yyyy-mm-dd: "), "%Y-%m-%d").date()
            except ValueError:
                print("Please enter a valid date")
                date = None

        category = input("Please enter the category of the expense: ")
        description = input("Please enter the description of the expense: ")

        amount = 0
        while amount <= 0:
            try:
                amount = float(input("Please enter the amount of the expense: "))
            except ValueError:
                print("Please enter a valid amount.")
                amount = 0

        new_expense = Expense(date, category, description, amount)
        self.expenses.append(new_expense)

    def remove_expense(self):
        selection = input("Enter id/description to remove: ")
        expense = self.find_expense(selection)
        if expense:
            self.expenses.remove(expense)
            print(f"Expense deleted from expenses!")
        else:
            print(f"Expense not found!")

    def find_expense(self, string):
        for expense in self.expenses:
            if string.lower() in expense.id.lower() or string.lower() in expense.description.lower():
                return expense
        return None

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def summary(self):
        total_expenses = 0
        category_expenses = dict()

        for expense in self.expenses:
            total_expenses += expense.amount
            category_expenses[expense.category] = category_expenses.get(expense.category, 0) + expense.amount

        print(f"Total expenses: {total_expenses} \n"
              f"Expenses by category:\n")

        for category, amount in category_expenses.items():
            print(f"{category}: {amount}\n")
