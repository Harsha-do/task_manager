tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
