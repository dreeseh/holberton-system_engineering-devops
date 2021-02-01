#!/usr/bin/python3
"""using given REST API:
https://jsonplaceholder.typicode.com/
for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1]))

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(argv[1]))

    dict_users = users_data.json()
    dict_todos = todo_list.json()
    employee_name = dict_users['name']
    done_tasks = []
    completed_tasks = 0
    total_tasks = 0

    for key in dict_todos:
        if key.get('completed') is True:
            completed_tasks += 1
            done_tasks.append(key.get('title'))
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name,
                 completed_tasks,
                 total_tasks))

    for key in done_tasks:
        print("\t {}".format(key))
