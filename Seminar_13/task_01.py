def getnumber():
    while True:
        try:
            number = float(input("Введите число: "))
            return number
        except ValueError:
            print("Введено не число")

numb = getnumber()
print(f'Вы ввели: {numb}')