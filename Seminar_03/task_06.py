my_string = input('введите строку').split()

my_string.sort()
print(my_string)

longest = len(max(my_string, key=len))  # max возвращает самую длиную строку
# longest = len(max(my_string))
for num, element in enumerate(my_string, 1):
    print(f'{num} {element:>{longest}}')