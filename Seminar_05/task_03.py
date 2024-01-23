text = 'asiopdufh'

dict_1 = {item: ord(item) for item in text}

d = iter(dict_1.items())

for _ in range(5):
    print(next(d))