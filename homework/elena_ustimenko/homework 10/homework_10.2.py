def repeat_me(func):
    def wrapper(*args, count):
        x = 0
        while x < count:
            func(*args)
            x+=1

    return wrapper


@repeat_me
def print_text(text):
    print(text)


print_text('123', count=5)
