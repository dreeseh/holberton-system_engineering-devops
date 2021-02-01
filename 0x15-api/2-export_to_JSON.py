#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import json
import requests
from sys import argv


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