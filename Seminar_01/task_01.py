n, e = int(input()), int(input())
sum = 0

for i in range(2, n + 1, 2):
    if i % e != 0:
        sum += i
print(sum) 