# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. 
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков

numbers = [1, 3, 5, 8, 9, 7, 1, 3]
un_numbers = list(set(numbers))
print(un_numbers)

numbers_01 = [1, 3, 5, 8, 9, 7, 1, 3]
uni_numbers = []
for number in numbers_01:
    if number not in uni_numbers:
        uni_numbers.append(number)
print(uni_numbers)        