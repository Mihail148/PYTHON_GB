# Создайте вручную список с повторяющимися элементами. 
# Удалите из него все элементы, которые встречаются дважды.

lst = [1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 1, 5, 2]

for i in set(lst):
    if lst.count(i) > 1:
        for j in range(lst.count(i)):
            lst.remove(i)
            
print(lst)            