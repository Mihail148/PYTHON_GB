a = 1
b = -6
c = 13

D = complex(b**2 - 4*a*c, 0)
x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)
print(D, x1, x2)