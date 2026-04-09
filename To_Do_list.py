task = []

def add_task(n):
    task.append(n)

def view_task():
    if not task:
        print("No tasks available.")
    else:
        for i, t in enumerate(task):
            print(f"{i}: {t}")

def delete_task(index):
    if 0 <= index < len(task):
        removed = task.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid index")

while True:
    print("\nWhat would you like to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        n = input("Enter a task: ")
        add_task(n)

    elif choice == "2":
        view_task()

    elif choice == "3":
        try:
            index = int(input("Enter task index to delete: "))
            delete_task(index)
        except ValueError:
            print("Please enter a valid number")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
