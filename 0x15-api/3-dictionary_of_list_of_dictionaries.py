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
