#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
from sys import argv as arg
import json


if __name__ == '__main__':

    the_id = arg[1]

    # create api_todos dictionary
    api_todos_dict = {'userId': arg}

    # and add it to the url
    todos_url = get('https://jsonplaceholder.typicode.com/todos',
                    params=api_todos_dict)
    todos = todos_url.json()

    # create api_user dictionary
    api_user_dict = {'id': arg}

    # add it to url
    user_url = get('https://jsonplaceholder.typicode.com/users',
                   params=api_user_dict)
    user = user_url.json()

    # find the value of the employee_name
    username = user[0].get('username')

    # to create a list of dictionaries
    task = [{"task": task.get('title'), "completed": task.get('completed'),
             "username": username} for task in todos]

    # create an other dictionary, using userId and store the task value in it
    my_dict = {}
    my_dict[the_id] = task

    # create a json file
    j_file = '{}.json'.format(the_id)

    with open(j_file, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f)
