#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users').json()

with open("todo_all_employees.json", 'w') as f:
        json.dump({user.get("id"): [{
            "task": O.get("title"),
            "complted": O.get("completed"),
            "username": user.get("username")
        } for O in requests.get(url + "todos",
                                params={'userId': user.get("id")}).json()]
        for user in users}, f)
