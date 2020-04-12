import numpy as np
from math import sin
from math import exp
from scipy import optimize
from matplotlib import pylab as plt

def f(x):
    return (sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2))

def h(x): # step function
    return int(f(x))


print(optimize.minimize(h, 30, method='BFGS'))
print()
print(optimize.differential_evolution(h, [(1, 30)]))

# show function graph
arg = np.arange(1, 30, 1)
y = np.sin(arg / 5) * np.exp(arg / 10) + 5 * np.exp(-arg / 2)
plt.step(arg, y)
plt.show()