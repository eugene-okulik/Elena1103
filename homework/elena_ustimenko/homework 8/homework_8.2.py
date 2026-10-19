def fibonachi_progression(limit=100):
    first_num = 0
    second_num = 1
    num = 0
    count = 0
    while count < limit:
        if count == 0:
            yield first_num
            count += 1
        elif count == 1:
            yield second_num
            count += 1
        else:
            num = first_num + second_num
            yield num
            count += 1
            first_num = second_num
            second_num = num


count = 0

for number in fibonachi_progression(100000):
    if count == 4:
        print(number)
    elif count == 199:
        print(number)
    elif count == 999:
        print(number)
    elif count == 99999:
        print(number)
        break

    count += 1
