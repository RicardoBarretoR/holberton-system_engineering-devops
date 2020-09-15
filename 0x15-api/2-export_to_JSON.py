#!/usr/bin/python3
""" export data in the JSON format"""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.json".format(user_id), 'w', newline="") as f:
        json.dump({user_id: [{
            "task": O.get("title"),
            "complted": O.get("completed"),
            "username": username
        } for O in todos]}, f)
