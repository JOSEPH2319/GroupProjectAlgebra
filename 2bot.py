import math

a = 1
b = 3
c = 2

d = math.pow(b,2) - 4 * a * c

d =  math.sqrt(d)

x1 = (-b + d)/(2 * a)
x2 = (-b - d)/(2 * a)

print(x1, x2)
