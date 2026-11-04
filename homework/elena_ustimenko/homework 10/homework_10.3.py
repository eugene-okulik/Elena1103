first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))


def arithmetic(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
            rezult = func(first, second, operation)
            return rezult
        elif first == second:
            operation = '+'
            rezult = func(first, second, operation)
            return rezult
        elif first > second:
            operation = '-'
            rezult = func(first, second, operation)
            return rezult
        elif second > first:
            operation = '/'
            rezult = func(first, second, operation)
            return rezult
    return wrapper


@arithmetic
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(first, second))
