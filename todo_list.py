import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
        self.created_at = datetime.datetime.now()

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Due: {self.due_date}, Priority: {self.priority})"


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print("✔ Task added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\n--- To-Do List ---")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("✔ Task marked as completed.")
        else:
            print("✖ Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("✔ All tasks cleared.")

    def edit_task(self, index, title=None, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority
            print("✔ Task updated.")
        else:
            print("✖ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            print(f"✔ Task '{deleted.title}' deleted.")
        else:
            print("✖ Invalid task number.")
