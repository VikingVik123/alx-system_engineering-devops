#!/usr/bin/python3
"""
Script to parse our output to a json file
"""
import json
import requests
import sys

if __name__ == "__main__":
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as employee ID")
        sys.exit(1)

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details based on the provided employee ID
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)
    user = user_response.json()

    # Fetch todo list for the specified user
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}.")
        sys.exit(1)
    todos = todos_response.json()

    # Export tasks to JSON
    data = {str(employee_id): [{"task": task['title'], "completed": task['completed'], "username": user['username']} for task in todos]}
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(data, f)

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    
    for task in completed:
        print("\t {}".format(task))
