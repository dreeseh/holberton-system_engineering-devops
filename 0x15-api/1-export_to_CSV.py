#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    users_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1])).json()

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(argv[1])).json()

    employee_name = users_data['name']
    completed_tasks = 0
    total_tasks = 0

    with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for key in todo_list:
            writer.writerow([
                key.get('userId'),
                users_data.get('username'),
                key.get('completed'),
                key.get('title')
            ])
