import numpy as np
from math import sin
from math import exp
from scipy import optimize
from matplotlib import pylab as plt

def f(x):
    return (sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2))

print(optimize.minimize(f, 2, method='BFGS'))
print()
print(optimize.minimize(f, 30, method='BFGS'))


# show function graph
arg = np.arange(1, 30, 0.1)
y = np.sin(arg / 5) *np.exp(arg / 10) + 5 * np.exp(-arg / 2)
plt.plot(arg, y)
plt.show()