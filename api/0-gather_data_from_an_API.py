#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
from sys import argv as arg


if __name__ == '__main__':

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

    # define the variables
    EMPLOYEE_NAME = None
    TOTAL_NUMBER_OF_TASKS = 0
    completed = 0
    NUMBER_OF_DONE_TASKS_title = []

    # find the value of the employee_name
    EMPLOYEE_NAME = user[0].get('name')

    # The script must accept an integer as a parameter which is the employee ID
    for j in todos:
        if j.get('userId') == int(arg[1]):
            # to add total number of tasks
            TOTAL_NUMBER_OF_TASKS += 1
            if j.get('completed') is True:
                # to add number of done tasks
                completed += 1
                NUMBER_OF_DONE_TASKS_title.append(j.get('title'))


    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          completed,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))

    for i in NUMBER_OF_DONE_TASKS_title:
        print("{} {}".format('\t', i))
