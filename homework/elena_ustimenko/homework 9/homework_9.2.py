temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
    27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_temperatures = filter(lambda x: x > 28, temperatures)

hot_temp_list = list(hot_temperatures)

max_temp = max(hot_temp_list)
min_temp = min(hot_temp_list)
middle_temp = sum(hot_temp_list) / len(hot_temp_list)

print(f'Максимальная температура из жаркого списка {max_temp}')
print(f'Минимальная температура из жаркого списка {min_temp}')
print(f'Средняя температура из жаркого списка {int(middle_temp)}')
