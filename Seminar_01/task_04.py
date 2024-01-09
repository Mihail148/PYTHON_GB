height = int(input('Введите количество рядов: '))

# 1 variation
for i in range(height):
    print(f'{'*' * (2 * i + 1): ^{height * 2}}')  
print('')

# 2 variation
n = 1
while n <= height * 2:
    print(('*' * n).center(height * 2))
    n += 2
print('')

# 3 variation
i = 0
while i < height:
    j = 0
    while j < height - 1 - i:
        print(' ', end='')
        j += 1
    j = 0
    while j < 2 * i + 1:
        print('*', end='')
        j += 1
    print('')
    i += 1    