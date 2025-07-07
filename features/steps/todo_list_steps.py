from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty")
def step_impl(context):
    context.manager = ToDoListManager()

@given('the to-do list has at least one task')
def step_impl(context):
    context.manager = ToDoListManager()
    context.manager.add_task("Sample Task", "Some description", "2025-07-10", "Medium")

@given('the to-do list has several tasks')
def step_impl(context):
    context.manager = ToDoListManager()
    context.manager.add_task("Task A", "Desc A", "2025-07-10", "Low")
    context.manager.add_task("Task B", "Desc B", "2025-07-11", "Medium")
    context.manager.add_task("Task C", "Desc C", "2025-07-12", "High")

@given('the to-do list has a task titled "{title}"')
def step_impl(context, title):
    context.manager = ToDoListManager()
    context.manager.add_task(title, "Description", "2025-07-10", "Medium")

@when('I add a task with title "{title}", description "{description}", due date "{due_date}" and priority "{priority}"')
def step_impl(context, title, description, due_date, priority):
    context.manager.add_task(title, description, due_date, priority)

@when('I list the tasks')
def step_impl(context):
    context.output = [str(task) for task in context.manager.tasks]

@when('I mark the task "{title}" as completed')
def step_impl(context, title):
    for index, task in enumerate(context.manager.tasks):
        if task.title == title:
            context.manager.mark_completed(index)
            return
    raise Exception("Task not found")

@when("I clear the to-do list")
def step_impl(context):
    context.manager.clear_tasks()

@when('I change the title to "{new_title}"')
def step_impl(context, new_title):
    if not context.manager.tasks:
        raise Exception("No tasks to edit")
    context.manager.edit_task(0, title=new_title)

@when('I delete the task titled "{title}"')
def step_impl(context, title):
    for index, task in enumerate(context.manager.tasks):
        if task.title == title:
            context.manager.delete_task(index)
            return
    raise Exception("Task not found to delete")

@then('the task list should contain a task titled "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.manager.tasks]
    assert title in titles, f"Task '{title}' not found in list"

@then('the task list should not contain a task titled "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.manager.tasks]
    assert title not in titles, f"Task '{title}' was not deleted"

@then("the task list should be empty")
def step_impl(context):
    assert len(context.manager.tasks) == 0, "Task list is not empty"

@then("I should see a list of all tasks with their titles")
def step_impl(context):
    assert len(context.output) > 0
    for line in context.output:
        assert isinstance(line, str)
