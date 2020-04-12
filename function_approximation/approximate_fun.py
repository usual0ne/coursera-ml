import numpy as np
from math import sin
from math import exp
from matplotlib import pylab as plt

def f(x):
    return round((sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)), 2)

# 1 4 10 15 - points on X axis
a = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([f(1), f(4), f(10), f(15)])
x = np.linalg.solve(a, b)

print("Matrix A:\n", a)
print("Vector b:\n", b)
print("Solution:\n", x)

print("Proof of the solution: a.dot(x)")
print(a.dot(x))

# true function graph
arg = np.arange(1, 15, 0.1)
y = np.sin(arg / 5) *np.exp(arg / 10) + 5 * np.exp(-arg / 2)
plt.plot(arg, y)
plt.show()

# approximate function graph
arg = np.array([1, 4, 10, 15])
y = np.array([f(1), f(4), f(10), f(15)])
plt.plot(arg, y)
plt.show()