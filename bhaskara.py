import math

a = int(input('Insira o valor de X '))
b = int(input('Insira o valor de y' ))
c = int(input('Insira o valor de z' ))
delta = b^2 - (-4*a*c)
print(delta)
x1 = -b + math.sqrt(delta) /(2*a)
x2 = -b - math.sqrt(delta) /(2*a)
print(x1,x2)
