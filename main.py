import time


def decorator(old_function):
    def new_function():
        start = (time.ctime())
        with open('time.log', 'a') as file:
            file.write(f' {old_function.__name__} started at {start}')

    return new_function


@decorator
def foo():
    print('Вызвана функция')


foo()
