import os
# the menu list of which to chose from
def show_menu():
    print("To-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "[X] " + tasks[task_number - 1][4:]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{deleted_task.strip()}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass  # Create an empty file if it doesn't exist
    main()
