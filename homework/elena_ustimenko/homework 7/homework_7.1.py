def guess_number(a):


    while True:
        input_number = int(input('Enter a number and try to guess: '))
        if input_number == a:
            print("Поздравляю! Вы угадали!")
            break
        elif input_number != a:
            print("попробуйте снова")
