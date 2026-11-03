def add_finish_log(func):
    def wrapper(*args):
        result = func(*args)
        print(f'finished')
        return result

    return wrapper


@add_finish_log
def example(text, number):
    print(text, number)

example('123', 4)
