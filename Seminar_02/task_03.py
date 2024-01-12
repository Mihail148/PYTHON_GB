import decimal

diameter = float(input())
decimal.getcontext().prec = 48

radius = decimal.Decimal(diameter / 2)
PI = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
area = PI * radius ** 2
length = 2 * PI * radius
print(f'{area}')
print(f'{length}')
