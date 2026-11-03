first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))


def arithmetic(func):
     def wrapper(first, second):
         if first < 0 or second < 0:
             return first * second
         elif first == second:
             return first + second
         elif first > second:
             return first - second
         elif second > first:
             return first / second

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
