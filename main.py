from expenseList import ExpenseList

expenses = ExpenseList()

while True:
    print(f"Select an option below")
    print(f"1. Add an expense")
    print(f"2. Remove an expense")
    print(f"3. View all expenses")
    print(f"4. View expense summary")
    print(f"5. Exit\n")
    option = input()

    match option:
        case "1":
            expenses.add_expense()
        case "2":
            expenses.remove_expense()
        case "3":
            expenses.view_expenses()
        case "4":
            expenses.summary()
        case "5":
            break
