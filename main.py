from todo_list import ToDoListManager

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear All Tasks")
    print("5. Edit Task")
    print("6. Delete Task")
    print("7. Exit")

def main():
    manager = ToDoListManager()

    while True:
        show_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            title = input("Task Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, description, due_date, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            try:
                task_num = int(input("Task number to mark as completed: ")) - 1
                manager.mark_completed(task_num)
            except ValueError:
                print("✖ Please enter a valid number.")

        elif choice == "4":
            manager.clear_tasks()

        elif choice == "5":
            try:
                task_num = int(input("Task number to edit: ")) - 1
                print("Leave fields blank to keep current value.")
                title = input("New Title: ").strip() or None
                description = input("New Description: ").strip() or None
                due_date = input("New Due Date (YYYY-MM-DD): ").strip() or None
                priority = input("New Priority (Low/Medium/High): ").strip() or None
                manager.edit_task(task_num, title, description, due_date, priority)
            except ValueError:
                print("✖ Please enter a valid number.")

        elif choice == "6":
            try:
                task_num = int(input("Task number to delete: ")) - 1
                manager.delete_task(task_num)
            except ValueError:
                print("✖ Please enter a valid number.")

        elif choice == "7":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("✖ Invalid option. Try again.")


if __name__ == "__main__":
    main()
