#!/usr/bin/python3
"""export data in the CSV format."""
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

    with open("{}.CSV".format(user_id), 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, O.get("completed"), O.get("title")]
        ) for O in todos]
