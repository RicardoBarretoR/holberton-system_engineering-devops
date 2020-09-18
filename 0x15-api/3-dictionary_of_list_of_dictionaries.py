#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    allTasks = {}
    for user in users:
        url = 'https://jsonplaceholder.typicode.com/todos?userId=' +\
               str(user['id'])
        tasks = requests.get(url).json()
        ls = []
        for task in tasks:
            dic = {}
            dic['task'] = task['title']
            dic['completed'] = task['completed']
            dic['username'] = user['username']
            ls.append(dic)
        allTasks[user['id']] = ls

    with open('todo_all_employees.json', 'w') as f:
        json.dump(allTasks, f)
