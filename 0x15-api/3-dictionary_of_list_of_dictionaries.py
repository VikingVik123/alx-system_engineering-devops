#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Dictionary to store tasks for all employees
    all_employee_tasks = {}

    # Fetch users
    users_response = requests.get(base_url + "users")
    if users_response.status_code != 200:
        print("Failed to fetch users.")
        exit(1)
    users = users_response.json()

    # Fetch tasks for each user
    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Fetch todo list for the user
        todos_response = requests.get(base_url + "todos", params={"userId": user_id})
        if todos_response.status_code != 200:
            print(f"Failed to fetch TODO list for user ID {user_id}.")
            continue
        todos = todos_response.json()

        # Append tasks to the dictionary
        all_employee_tasks[user_id] = [{"username": username, "task": task['title'], "completed": task['completed']} for task in todos]

    # Export tasks to JSON
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employee_tasks, f)

    print("Tasks for all employees exported to todo_all_employees.json")
