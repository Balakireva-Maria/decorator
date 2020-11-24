import time
import os

import time
import os

a = os.getcwd()


def decorator(old_function):
    def new_function(*args, **kwargs):
        start = (time.ctime())
        with open('time.log', 'a') as file:
            file.write(f' {old_function.__name__} started at {start}, path to log file is {a} ')

    return new_function


@decorator
def foo(a):
    print('Вызвана функция')


foo(a)