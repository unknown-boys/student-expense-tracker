import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    category = input("Category: ")
    amount = float(input("Amount: "))
    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for expense in expenses:
        print(f"{expense['category']}: ${expense['amount']:.2f}")
        total += expense["amount"]

    print(f"\nTotal Spent: ${total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
