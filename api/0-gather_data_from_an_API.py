#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
import sys


if __name__ == '__main__':

    api_todos = get('https://jsonplaceholder.typicode.com/todos')
    response = api_todos.json()
    response.json()

    api_user = get('https://jsonplaceholder.typicode.com/users')
    response = api_user.json()
    response.json()

    # define variables
    EMPLOYEE_NAME = 0
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    arg = sys.argv[1]

    # The script must accept an integer as a parameter which is the employee ID

    if type(arg) == int:
        for i in api_user:
            if i.id == arg:
                EMPLOYEE_NAME = i.name

        for j in api_todos:
            # to add total number of tasks
            if j.id == arg:
                TOTAL_NUMBER_OF_TASKS += 1

            if j.completed is True:
                # to add number of done tasks
                j.completed += 1
                NUMBER_OF_DONE_TASKS = j.title

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))

    for i in NUMBER_OF_DONE_TASKS:
        print("\t ".format(NUMBER_OF_DONE_TASKS))
