tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    print("\nTasks:")
    for task in tasks:
        print("-", task)

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")