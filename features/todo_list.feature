Feature: To Do List Management
  As a user
  I want to manage tasks in a to-do list
  So that I can keep track of what I need to do

  Scenario: Add a new task to the to-do list
    Given the to-do list is empty
    When I add a task with title "Buy groceries", description "Milk and bread", due date "2025-07-08" and priority "High"
    Then the task list should contain a task titled "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list has at least one task
    When I list the tasks
    Then I should see a list of all tasks with their titles

  Scenario: Mark a task as completed
    Given the to-do list has a task titled "Study for exam"
    When I mark the task "Study for exam" as completed
    Then the task "Study for exam" should be marked as completed

  Scenario: Clear the entire to-do list
    Given the to-do list has several tasks
    When I clear the to-do list
    Then the task list should be empty

  Scenario: Edit a task
    Given the to-do list has a task titled "Finish homework"
    When I change the title to "Finish math homework"
    Then the task list should contain a task titled "Finish math homework"

  Scenario: Delete a task
    Given the to-do list has a task titled "Call the dentist"
    When I delete the task titled "Call the dentist"
    Then the task list should not contain a task titled "Call the dentist"

