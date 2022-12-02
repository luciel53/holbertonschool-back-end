#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
 information about his/her TODO list progress.
"""
from requests import get
import sys


if __name__ == '__main__':

    arg = sys.argv[1]

    #create api_todos dictionary
    api_todos_dict = {'userId': arg}

    # and add it to the url
    todos_url = get('https://jsonplaceholder.typicode.com/todos', params=api_todos_dict)
    response = todos_url.json()
    user = response.json()

    # create api_user dictionary
    api_user_dict = {'id': arg}

    # add it to url
    user_url = get('https://jsonplaceholder.typicode.com/users', params=api_user_dict)
    response = user_url.json()
    todos = response.json()

    # define variables
    EMPLOYEE_NAME = 0
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    # find the value of employee_name
    EMPLOYEE_NAME = user[0].get('name')

    # The script must accept an integer as a parameter which is the employee ID

    for j in todos:
        # to add total number of tasks
        if j.get('completed') is True:
            # to add number of done tasks
                j.completed += 1
                NUMBER_OF_DONE_TASKS.append(j.get('title'))
        TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))

    for i in NUMBER_OF_DONE_TASKS:
        print("{} {}".format('\t', i))
