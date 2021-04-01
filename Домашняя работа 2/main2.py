import time
import os
log_path = os.getcwd()



def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            print('Будет вызвана функция')
            result = foo(*args, **kwars)
            start = (time.ctime())
            with open('time.log', 'a', encoding='utf-8') as file:
                file.write(f' {new_foo.__name__} started at {start}, path to log file is {args} ')
            return result

        return new_foo

    return decor


@parametrized_decor(parameter=log_path)
def foo(parametr):
    return ('вызвана функция')

foo(log_path)