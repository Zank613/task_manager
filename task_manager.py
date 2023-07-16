import csv ,operator
import os

# Task class for adding attribute.
class Task:
    def __init__(self, name: str, deadline: float, description: str, priority=0):
        self.name = name
        self.deadline = deadline
        self.description = description
        self.priority = priority
    # Tasks did not print out as readable so i did this.
    def __repr__(self):
        return f"Name: {self.name}\nDeadline: {self.deadline}\nDescription: {self.description}\nPriority: {self.priority}\n"


# Class to manage Tasks.
class TaskManager:
    def __init__(self, file_path):
        self.tasks = []
        self.file_path = file_path
        self.load_from_csv()

    # Method to load data from .csv file.
    def load_from_csv(self):
        # Checks if there is a file called task_table.csv if not, this method creates one.
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Deadline', 'Description', 'Priority'])
                
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.tasks = [Task(*row) for row in reader]

    def add_new(self, name, deadline, description, priority):
        new_task = Task(name, deadline, description, priority)
        self.tasks.append(new_task)

    def remove_task(self, name):
        found = False
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                found = True
                break

        if found:
            self.write_to_csv("task_table.csv")
            print("Task removed successfully.")
        else:
            print("No task with the given name found.")

    
    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def write_to_csv(self, filename):
        with open (filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Deadline', 'escription', 'Priority'])
            for task in self.tasks:
                writer.writerow([task.name, task.deadline, task.description, task.priority])
        f.close()

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    # This editing method took me hours to make.
    def edit_task(self, name):
        task = self.get_task_by_name(name)
        if task is not None:
            attribute = input("Please enter which attribute you would like to change.\nName, Deadline, Description or Priority\n>")
            if attribute == 'name':
                new_name = input("Enter the new name: ")
                task.name = new_name
            elif attribute == 'deadline':
                new_deadline = input("Enter the new deadline: ")
                try:
                    new_deadline = float(new_deadline)
                    task.deadline = new_deadline
                except ValueError:
                    print('Invalid deadline value. Please enter a valid float value.')
            elif attribute == 'description':
                new_description = input("Please enter the new description: ")
                task.description = new_description
            elif attribute == 'priority':
                new_priority = input("Please enter the new priority: ")
                try:
                    new_priority = int(new_priority)
                    task.priority = new_priority
                except ValueError:
                    print("Invalid priority value. Please enter a valid integer value.")
            else:
                print('Invalid attribute.')
                return

            self.write_to_csv("task_table.csv")
            print("Task edited successfully.")
        else:
            print("No task with the given name found.")

        
# Calling TaskManager class to manager varible.
manager = TaskManager("task_table.csv")

# This whole loop is menu system.
while True:
    print("\n")
    print("--- TASK MANAGER ---")
    user_choice = input("A.Add a new task\nB.Remove a task\nC.Edit a task\nD.View Tasks\nE.Quit\n>")
    user_choice = user_choice.upper()
    if user_choice == "A":
            user_choice2 = input("Enter a title for task:\n>")
            user_choice3 = input("Enter a deadline for the task (DD/MM):\n>")
            try:
                user_choice3 = float(user_choice3)
            except ValueError:
                print("Invalid deadline format.")
                continue

            user_choice4 = input("Enter a description for the task:\n>")
            user_choice5 = input("Set a priority for the task.:\n>")
            try:
                user_choice5 = int(user_choice5)
            except ValueError:
                print("Invalid priority value.")
                continue

            manager.add_new(user_choice2, user_choice3, user_choice4, user_choice5)
            manager.write_to_csv("task_table.csv")

    # User choice system to remove.
    elif user_choice == "B":
        user_choice6 = input("Please enter which task would you like to remove.\n>")
        manager.remove_task(user_choice6)
    
    # User choice system to edit tasks.
    elif user_choice == "C":
        user_choice7 = input("Please enter which task would you like to edit.\n>")
        manager.edit_task(user_choice7)

    # User choice system to view tasks.
    elif user_choice == "D":
        manager.view_tasks()

    # Quitting the loop also means quitting program as there is nothing else to run.
    elif user_choice == "E":
        print("Quitting the program.")
        break

    # If anything goes wrong, you are returning to start of the loop again.
    else:
        print('Invalid value. Returning to main menu')
        print("\n")
        continue
