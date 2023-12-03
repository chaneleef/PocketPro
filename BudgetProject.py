# BudgetProject.py
"""
Objective: Create a budgeting tracker app.

Elements we want to include:
1. A welcome message
2. Ask the user for their name
3. A menu with the following options:
    a. Add an expense
    b. Add a budget goal
    c. View past expenses
    d. View budget goals
    e. Personalized plausible budget
    f. Tips for budgeting
    g. Quit
4. Closing message
"""


# Bold text function
def bold_text(text):
    start = '\033[1m'
    end = '\033[0m'
    return start + text + end


# Function to display the main menu and get user choice
def open_menu():
    print(bold_text("Menu"))
    print("a. Add expenses")
    print("b. Add a budget goal")
    print("c. View past expenses")
    print("d. View budget goals")
    print("e. Budget Summary")
    print("f. Tips for budgeting")
    print("g. Quit\n")

    choice = input("Enter your choice: ").lower()
    while choice not in ["a", "b", "c", "d", "e", "f", "g"]:
        print("Invalid choice. Please try again.")
        print("Enter a, b, c, d, e, f, or g.\n")
        choice = input("Enter your choice: ").lower()

    return choice


# Function to add expenses
def add_expense(existing_expenses=None):
    if existing_expenses is None:
        existing_expenses = {}

    while True:
        try:
            num_expenses = int(input("How many expenses would you like to add? "))

            if num_expenses >= 0:
                break
            else:
                print(bold_text("Please enter a positive integer.\n"))
        except ValueError:
            print(bold_text("Invalid input. Please enter a positive integer.\n"))

    for _ in range(num_expenses):
        expense_name = input("Enter expense name: ")
        while True:
            try:
                expense_amount = float(input("Enter expense amount for {}: ".format(expense_name)))
                if expense_amount > 0:
                    break
                else:
                    print("Please enter a positive amount.\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        existing_expenses[expense_name] = expense_amount
        print()

    return existing_expenses



# Function to view expenses
def view_expenses(expenses):
    total_spending = sum(expenses.values())

    if expenses:
        print("List of Expenses:")
        for key, val in expenses.items():
            print(f"{key}: ${val:.2f}")
    else:
        print("No expenses added yet.")

    return total_spending

# User adds budget goal
def add_budget_goal():
    while True:
        try:
            budget_goal = float(input("What is your new budget goal? $"))
            if budget_goal >= 0:
                return budget_goal
            else:
                print(bold_text("Please enter a non-negative amount.\n"))
        except ValueError:
            print(bold_text("Invalid input. Please enter a valid number.\n"))


# Function to view the budget goal and progress
def view_budget_goal(budget_goal, expenses):
    if budget_goal is not None:
        print("Your budget goal is ${}".format(budget_goal))
        total_spending = sum(expenses.values())
        progress = budget_goal - total_spending

        if progress > 0:
            print("Congrats you are ${:.2f} under your budget goal!".format(progress))
        elif progress == 0:
            print("Notice: you've reached your budget goal.")
        else:
            print("You've exceeded your budget goal by ${:.2f}.".format(abs(progress)))
    else:
        print("No budget goal set yet.")


# Budget summary
def personalized_budget(expenses, budget_goal):
    total_spending = sum(expenses.values())
    remaining_budget = budget_goal - total_spending

    if remaining_budget < 0:
        print("Current Total Spending: ${:.2f}\n".format(total_spending))
        print(bold_text("You've exceeded your budget goal. Consider reducing expenses."))
    else:
        print(bold_text("Personalized Budget Plan:"))
        print("1. Current Total Spending: ${:.2f}\n".format(total_spending))
        print("2. Remaining Budget: ${:.2f}\n".format(remaining_budget))

        if remaining_budget > 0:
            print("3. Suggested Savings: Allocate " + str(round(remaining_budget*.1)) + "$ for savings.\n")
        else:
            print("3. Warning: You've reached your budget goal. Be cautious of additional spending.")


# Tips for budgeting
def tips_for_budgeting():
    print("1. Create your budget before the month begins\n" +
          "2. Use the right tools (PocketPro)\n" +
          "3. Establish needs versus wants\n" +
          "4. Keep bills and receipts organized\n" +
          "5. Prioritize debt repayment\n" +
          "6. Don’t forget to factor in fun\n" +
          "7. Save first, then spend\n" +
          "8. Start contributing to retirement now\n" +
          "9. Split your direct deposit\n" +
          "10. Prepare for the unexpected\n" +
          "11. Plan for large purchases\n" +
          "12. Adjust your budget monthly\n" +
          "13. Outline specific, realistic goals\n" +
          "14. Observe a no-spend day\n" +
          "15. Don’t be too hard on yourself\n" +
          "16. Try cash-only budgeting\n" +
          "17. Budget for your financial situation\n" +
          "18. Track your expenses\n" +
          "19. Be flexible")
    return None
