#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
import json


if __name__ == '__main__':

    user_url = get('https://jsonplaceholder.typicode.com/users')
    user = user_url.json()

    # create a new dictionary
    new_dict = {}

    for person in user:
        username = person.get('username')
        UserId = person.get('id')

        # create api_todos dictionary (!!! select the good ID)
        api_todos_dict = {'userId': UserId}

        # and add it to the url
        todos_url = get('https://jsonplaceholder.typicode.com/todos',
                        params=api_todos_dict)
        todos = todos_url.json()

        # to create a list of dictionaries
        task1 = [{"task": task.get('title'), "completed":
                                             task.get('completed'),
                                             "username": username}
                 for task in todos]

        # to store the list of dictionaries in the new dictionary
        new_dict[UserId] = task1

    # create a json file
    j_file = '{}.json'.format('todo_all_employees')

    with open(j_file, 'w', encoding='utf-8') as f:
        json.dump(new_dict, f)
