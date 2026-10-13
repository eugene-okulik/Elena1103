str_var_1 = 'результат операции: 42'
str_var_2 = 'результат операции: 514'
str_var_3 = 'результат работы программы: 9'


def result_number(text):

    number = int(text.split(': ')[1])
    print(number + 10)

result_number(str_var_1)
