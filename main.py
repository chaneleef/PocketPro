import BudgetProject as bp
# Pocket Pro: Budget Tracker App


# main function
def main():
    # initializes variables
    expenses = {}
    budget_goal = 0

    # welcome message
    print(bp.bold_text("Welcome to your personal Pocket Pro!\n"))

    # ask if the user would like to see a tutorial
    tutorial = input("Press any key then enter if you would like to see the tutorial:  ")
    if tutorial:
        print("\nYour Pocket Pro considers your monthly expenses and budget goal " +
              "to create a personalized budget plan! " + "Also see our exclusive budgeting tips!\n"
              + "\nOverview of features:\n" +
              "1. Enter your first name\n" + "2. select a menu option (a-f)\n"
              + "3. (a) add expenses option allows you to track monthly expenses "
              + "i.e. rent, groceries, subscriptions.\n" +
              "You can make changes to your expenses if you enter the name of the expense and enter the new value\n"
              + "4. (b) add a budget goal for the end of the month.\n" + "5. (c) (d) allows you to quick view your " +
              "total expenses for the month and current budget goal.\n" +
              "6. (f) Look at your personalized budget plan to learn the steps to reach your budget goal!\n" +
              "7. (g) You can always quit the app by going back to the menu and entering g!\n" +
              bp.bold_text("That's all for your Pocket Pro Tutorial!\n ")
              )

    # gets user's name and says hi
    name = input("What is your name? ")
    print(f"\nHi {name}! What would you like to do today?\n\n")

    # loop of choices
    while True:
        choice = bp.open_menu()

        if choice == "a":
            expenses.update(bp.add_expense(expenses))  # Update the existing expenses dictionary
            p = input("Would you like to add more expenses? (y/n) ").lower()
            print()
            while p == "y":
                expenses.update(bp.add_expense(expenses))  # Update the existing expenses dictionary
                p = input("Would you like to add more expenses? (y/n) ").lower()
                print()
            print(bp.bold_text("You're done adding expenses.\n"))

        elif choice == "b":
            budget_goal = bp.add_budget_goal()
            print("Your budget goal is now: ${}".format(budget_goal))

        elif choice == "c":
            total_spending = bp.view_expenses(expenses)
            print("\nTotal Expenses for the Month: ${:.2f}\n".format(total_spending))

        elif choice == "d":
            if budget_goal == 0:
                print(bp.bold_text("Please add a budget goal first before viewing."))
            else:
                bp.view_budget_goal(budget_goal, expenses)

        elif choice == "e":
            bp.personalized_budget(expenses, budget_goal)

        elif choice == "f":
            bp.tips_for_budgeting()

        another_choice = input("Would you like to go back to the main menu? (y/n) ").lower()
        print("\n\n\n_____________________________")
        if another_choice != "y" or choice == "g":
            print(bp.bold_text(f"Goodbye {name}! See you next time..."))
            break


if __name__ == "__main__":
    main()
