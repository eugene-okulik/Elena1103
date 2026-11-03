PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


price_list = PRICE_LIST.split('\n')
price_list2  = [x.split(' ') for x in price_list]

price_dict = {name: int(price.replace('р', '')) for name, price in price_list2}

print(price_list)
print(price_list2)
print(price_dict)
