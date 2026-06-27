import random
import json

class TodoApp:

    def __init__(self, tasks):
        self.tasks = tasks
    
    def has_task(self):
        if not self.tasks:
            print("\nNo tasks available!")
            return False
        return True
    
    def add_task(self, task_name):
        if not task_name:
            print("You can't add empty task!")
            return
    
        if any(task['task'].lower() == task_name.lower() for task in self.tasks):
            print("\nYou already have added this task!")
            return
        self.tasks.append({"task": task_name, "status": False, 'priority': None})
        print("\nTask has been added successfully!")

    def view_tasks(self):
        if not self.has_task():
            return

        print("\nShowing tasks")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["status"] else "✗"
            print(f"{idx}. Task: {task['task']}\n   Done: {status}\n   Priority: {task['priority']}")

    def select_task(self):
        if not self.has_task():
            return
    
        self.view_tasks()
        try:
            task = int(input("\nEnter the number of the task: "))
            if 1 <= task <= len(self.tasks):
                return task - 1
        except ValueError:
            pass

        print("Invalid selection")
        return None
    
    def mark_as_completed(self):
        idx = self.select_task()
        if idx is None:
            return 
        self.tasks[idx]['status'] = not self.tasks[idx]['status']
        status = "completed" if self.tasks[idx]['status'] else "incomplete"
        print(f"Task marked as {status}")
    
    def remove_task(self):
        idx = self.select_task()
        if idx is None:
            return
        removed = self.tasks.pop(idx)
        print(f"\nRemoved task: {removed['task']}")

    def edit_task(self):
        idx = self.select_task()
        if idx is None:
            return
    
        update_task = input("Change the task: ").strip()
        if not update_task:
            print("Task cannot be empty")
            return

        old_task = self.tasks[idx]['task']
        self.tasks[idx]['task'] = update_task
        print(f"{old_task} has been updated to {self.tasks[idx]['task']}")
    
    def do_random_task(self):
        if not self.has_task():
            return
    
        print("\nChallenge for you:")
        temp_task = [task['task'] for task in self.tasks if not task['status']]
 
        if temp_task:
            print(f"\nDo this task now!: {random.choice(temp_task)}")
        else:
            print("No task available!")
    
    def set_priority(self):
        idx = self.select_task()
        if idx is None:
            return
        try:
            priority = int(input("Select the priority (1=High, 2=Medium, 3=Low): "))    
            if not self.tasks[idx]['status']:
                if priority == 1:
                    self.tasks[idx]['priority'] = "High"
                elif priority == 2:
                    self.tasks[idx]['priority'] = "Medium"
                elif priority == 3:
                    self.tasks[idx]['priority'] = "Low"
                else:
                    print("Please enter 1, 2 or 3 to set the priority")
        except ValueError:
            print("Only numbers please!")

    def search_task(self):
        search_term = input("Enter your task name to search it: ").strip().lower()
        for idx, task in enumerate(self.tasks, start=1):
            if search_term in task['task'].lower():
                print(f"{idx}. {task['task']}")

    def save_task(self):
        try:
            with open("tasks.json", "w") as f:
                json.dump(self.tasks, f, indent=4)
                print("Tasks saved successfully.")
        except OSError:
            print("Failed to save!")
    
    def load_tasks(self):   
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

