import random

def salary_bonus():
    salary = int(input('Enter you salary please: '))
    bonus_sum = random.randint(1, 5000)
    bonus = [True, False]
    rezult = random.choice(bonus)

    if rezult:
            salary_with_bonus = salary + bonus_sum
    else:
            salary_with_bonus = salary

    return salary, rezult, str(f'${salary_with_bonus}')

print(salary_bonus())
