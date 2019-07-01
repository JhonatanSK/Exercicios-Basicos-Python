from math import sqrt

a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))

delta = (b**2 -4*a*c)
raizDelta = sqrt(delta)

x1 = int((-b + raizDelta)/2*a)
x2 = int((-b - raizDelta)/2*a)

print(x1, x2)