#!/usr/bin/python3
"""using given REST API:
https://jsonplaceholder.typicode.com/
for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import requests

employee_id = argv[1]

users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.
    format(employee_id))

todo_list = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.
    format(employee_id))

dict_users = users_data.json()
dict_todos = todo_list.json()
employee_name = dict_users['name']
completed_tasks = 0
total_tasks = 0

for done_tasks in dict_todos:
    if done_tasks.get('completed') is True:
        completed_tasks += 1
    total_tasks += 1

print("Employee {} is done with tasks({}/{})):".format(
       employee_name,
       completed_tasks,
       total_tasks))

for done_tasks in dict_todos:
    if done_tasks.get('completed') is True:
        print("\t {}".format(done_tasks.get('title')))
