expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added.")

    elif choice == "2":
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. ₹{expense}")

    elif choice == "3":
        print("Total Expense: ₹", sum(expenses))

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
