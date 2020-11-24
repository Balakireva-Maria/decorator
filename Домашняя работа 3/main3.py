import time

side = 3


def calculate():
    squares_perimeter = side * 4
    squares_square = side ** 2
    print('Периметр равен', squares_perimeter, 'Площадь равна', squares_square)
    lengh = int(input('Введите длину прямоугольника:'))
    width = int(input('Введите ширину прямоугольника:'))
    perimeter = lengh * 2 + width * 2
    square = lengh * width
    print('Периметр равен', perimeter, 'Площадь равна', square)


def decorator(old_function):
    def new_function():
        start = (time.ctime())
        with open('time.log', 'a') as file:
            file.write(f' {old_function.__name__} started at {start} \n')

    return new_function


@decorator
def calculate():
    print('press f to respect')


calculate()