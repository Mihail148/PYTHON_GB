from random import randint


def game(func):

    def wrapper(number_secret, count):
        if not 1 <= number_secret <= 100:
            number_secret = randint(1, 100)
        if not 1 <= count <= 10:
            count = randint(1, 10)
        return func(number_secret, count)
    print('Enter game()')
    return wrapper


@game
def run(number_secret: int, count: int):
    for _ in range(count):
        answer = int(input('Угадайте число: '))
        if number_secret == answer:
            return True
    return False


if __name__ == '__main__':
    run(7, 15)