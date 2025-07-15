'''
In this project, you will create a To-Do List management that uses various Python concepts such as object-oriented (OOP), reading and writing CSV files, and data management. The project includes the ability to add, delete, and view tasks, as well as save and load the to-do list from a file.

Project Features:

Add New Task: A new task is added to the list.

Remove Task: A task is removed from the list.

View To-Do List: All tasks in the list are displayed.

Save To-Do List to CSV File: All tasks are automatically saved to a CSV file.

Load from CSV File: The to-do list is automatically loaded from a CSV file.

Select Priority for Tasks: Each task can have a priority (e.g., high, medium, or low).

Project Details:

You should use object-oriented to manage tasks. Create classes for Task and ToDoList.
Use CSV file to store and load data.
The project should use context menu to perform various operations (add task, delete task, view tasks and save list).

Application structure:
Task class to model each task:
Each task can have name, description and priority.
ToDoList class to manage to-do list:
Add task to list
Remove task from list
Show all tasks
Save and load list from CSV file
'''

import csv
import os

# Task class
class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority.lower()  # normalize input

    def __str__(self):
        return f"[{self.priority.capitalize()}] {self.name} - {self.description}"


# ToDoList class
class ToDoList:
    def __init__(self, filename='todo.csv'):
        self.tasks = []
        self.filename = filename
        self.load_from_csv()

    def add_task(self, task):
        self.tasks.append(task)
        print("✅ Task added successfully.")

    def remove_task(self, task_name):
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.name != task_name]
        if len(self.tasks) < original_count:
            print("✅ Task removed.")
        else:
            print("⚠️ Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks in the list.")
        else:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def save_to_csv(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description', 'priority'])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print("💾 To-Do list saved to file.")

    def load_from_csv(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row['name'], row['description'], row['priority'])
                    self.tasks.append(task)
            print(f"📂 Loaded {len(self.tasks)} tasks from {self.filename}.")


# Menu system
def show_menu():
    print("\n🧭 MENU")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Save To-Do List")
    print("5. Exit")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option (1–5): ")

        if choice == '1':
            name = input("Task name: ")
            description = input("Task description: ")
            priority = input("Priority (high, medium, low): ")
            task = Task(name, description, priority)
            todo.add_task(task)

        elif choice == '2':
            task_name = input("Enter task name to remove: ")
            todo.remove_task(task_name)

        elif choice == '3':
            todo.view_tasks()

        elif choice == '4':
            todo.save_to_csv()

        elif choice == '5':
            todo.save_to_csv()
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
