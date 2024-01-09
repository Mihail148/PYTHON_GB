
while True:
    number = int(input('Введите число: '))
    if not 1 < number < 1000:
        continue
    if number < 10:
        res = number ** 2
    elif number < 100:
        res = (number // 10) * (number % 10)
    else:
        res = (number % 10 * 100) + (number // 10 % 10 * 10) + number // 100
    break

print(res)