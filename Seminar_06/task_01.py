import random
from sys import argv

def guess(min_numb, max_numb, count):
    numb_1 = random.randint(min_numb, max_numb)
    for i in range(count):
        numb = int(input('Enter number: '))
        if numb == numb_1:
            return True
        elif numb > numb_1:
            print('Number is higher than you enter')
        else:
            print('Number is lower than you enter')
    return False  

if __name__ == '__main__':
    print(guess(2, 5, 3))          