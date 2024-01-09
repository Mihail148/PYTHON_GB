year = int(input('Введите год: '))
MAIN_CONDITION = 4
ADD_CONDITION = 100
YEAR_EXCEM = 400

if (year % MAIN_CONDITION == 0 and year % ADD_CONDITION != 0 
        or year % YEAR_EXCEM == 0):
    res = 'Год +'
else:
    res = 'Год -'

print(res)