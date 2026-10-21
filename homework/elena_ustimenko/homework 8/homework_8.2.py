import sys


def fibonachi_progression():
    first_num = 0
    second_num = 1
    num = 0
    count = 0
    while True:
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


sys.set_int_max_str_digits(0)
count = 0

for number in fibonachi_progression():
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
