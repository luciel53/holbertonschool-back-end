#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
from sys import argv as arg
import csv


if __name__ == '__main__':

    var = arg[1]
    # create api_todos dictionary
    api_todos_dict = {'userId': var}

    # and add it to the url
    todos_url = get('https://jsonplaceholder.typicode.com/todos',
                    params=api_todos_dict)
    todos = todos_url.json()

    # create api_user dictionary
    api_user_dict = {'id': var}

    # add it to url
    user_url = get('https://jsonplaceholder.typicode.com/users',
                   params=api_user_dict)
    user = user_url.json()

    # find the value of the username
    username = user[0].get('username')
    # find the value of the userId and name the file
    file_user_id = '{}.csv'.format(var)

    with open(file_user_id, 'w', encoding='UTF8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for j in todos:
            writer.writerow((j.get("userId"), username, j.get("completed"),
                             j.get("title")))
