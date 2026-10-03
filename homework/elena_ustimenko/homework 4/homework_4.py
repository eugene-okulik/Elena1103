# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества

my_dict = {
    'tuple': (1, 2, True, 'four', 5.1, None),
    'list': [1, 2, False, 4, 'Five', 6],
    'dict': {1: 1, 'two': 'two', 3: 3, 'four': 'four', 5: 5, 'six': 'six'},
    'set': {1, 'Two', 7, False, 10, 'Zero'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(7)
my_dict['list'].pop(1)

print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = '12'
my_dict['dict'].pop(1)

print(my_dict['dict'])

my_dict['set'].add(15)
my_dict['set'].pop()

print(my_dict['set'])
