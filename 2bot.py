import math

a = 1
b = 3
c = 2

d = math.pow(b,2) - 4 * a * c

d =  math.sqrt(d)

x1 = (-b + d)/(2 * a)
x2 = (-b - d)/(2 * a)

print(x1, x2)



import matplotlib.pyplot as plt
import time
import numpy

def plot_linear_eq(a, b, clr):
  x = list(range(-10, 11)
  y = [(a*i + b) for i in x]
  plt.plot(x, y, label = 'linear', linestyle = '-', color = clr)

a = 0
b = 0
plot_linear_eq(a, b, 'r')
plt.show(block = False)
plt.close
