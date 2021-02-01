#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import json
import requests


users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users').json()

dictionary = {}

for key in users_data:
    new_todos = []
    todo_list = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(key.get('id'))).json()

    for key2 in todo_list:
        todo = {}
        todo['task'] = key2.get('title')
        todo['completed'] = key2.get('completed')
        todo['username'] = key.get('username')
        new_todos.append(todo)
    dictionary[key.get('id')] = new_todos

with open('todo_all_employees.json', mode='w') as jsonfile:
    json.dump(dictionary, jsonfile)

"""
users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.
    format(argv[1])).json()

todo_list = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.
    format(argv[1])).json()


employee_name = users_data['name']
completed_tasks = 0
total_tasks = 0

todos = []
for key in todo_list:
    todo = {}
    todo['task'] = key.get('title')
    todo['completed'] = key.get('completed')
    todo['username'] = users_data.get('username')
    todos.append(todo)

dictionary = {argv[1]: todos}

with open('{}.json'.format(argv[1]), mode='w') as jsonfile:
    json.dump(dictionary, jsonfile)
"""


"""
with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for key in todo_list:
        writer.writerow([
            key.get('userId'),
            users_data.get('username'),
            key.get('completed'),
            key.get('title')
        ])
"""
