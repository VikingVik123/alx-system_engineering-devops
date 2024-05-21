#!/usr/bin/python3
"""
Script that exports the  data to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the script is provided with the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

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
    username = user.get("username")

    # Fetch todo list for the specified user
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}.")
        sys.exit(1)
    todos = todos_response.json()

    # Filter out completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the progress summary for the employee
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    
    # Print the titles of the completed tasks
    for task in completed:
        print("\t {}".format(task))

    # Export data to CSV file
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow()
        for task in todos:
            writer.writerow([employee_id, username, task.get("completed"), task.get("title")])
