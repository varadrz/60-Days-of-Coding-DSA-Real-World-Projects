# Day 1 - Expense Analyzer (DSA Focused)
# Language: Python 3

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    print("Expense added successfully.\n")


def view_statistics(expenses):
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.\n")
        return

    total_expense = 0
    unique_days = set()
    category_map = {}

    for exp in expenses:
        total_expense += exp["amount"]
        unique_days.add(exp["date"])

        if exp["category"] in category_map:
            category_map[exp["category"]] += exp["amount"]
        else:
            category_map[exp["category"]] = exp["amount"]

    average_per_day = total_expense / len(unique_days)

    print("\n===== Expense Statistics =====")
    print(f"Total number of expenses: {len(expenses)}")
    print(f"Number of days recorded: {len(unique_days)}")
    print(f"Total Expense: ₹{total_expense:.2f}")
    print(f"Average Expense Per Day: ₹{average_per_day:.2f}")
    print("\nCategory-wise Expense:")
    for category, amount in category_map.items():
        print(f"  {category}: ₹{amount:.2f}")
    print()


def main():
    expenses = []  # Array (DSA)

    while True:
        print("===== Expense Analyzer =====")
        print("1. Add Expense")
        print("2. View Statistics")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_statistics(expenses)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
