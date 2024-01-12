number = 10
number_two = number
result = ''
while number != 0:
    result = str(number % 2) + result
    number //= 2
print(result)
print(bin(number_two))
    