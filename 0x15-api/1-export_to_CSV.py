#!/usr/bin/python3
"""export data in the CSV format."""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    username = requests.get(url).json()['username']
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    tasks = requests.get(url).json()
    with open(argv[1]+'.csv', 'w', newline='') as File:
        writer = csv.writer(File, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1]] + [username] +
                            [task['completed']] + [task['title']])
