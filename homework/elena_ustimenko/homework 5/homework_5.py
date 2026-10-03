# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

# Задание 2

string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

number_index = string_1.index(':') + 2

number = int(string_1[number_index:].strip())

result_1 = number + 10

print(result_1)

number_index = string_2.index(':') + 2

number = int(string_2[number_index:].strip())

result_2 = number + 10

print(result_2)

number_index = string_3.index(':') + 2

number = int(string_3[number_index:].strip())

result_3 = number + 10

print(result_3)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

print('Students ', ', '.join(students), 'study these subjects:', ', '.join(subjects))


