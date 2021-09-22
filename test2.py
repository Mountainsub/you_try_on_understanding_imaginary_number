import numpy as np
from matplotlib import pyplot as plt
def func():
    size = 100
    x = np.arange(size)
    y = np.zeros(size)
    y[0] = 1
    y[1] = 1.99
    for i in range(size-2):
        y[i+2] = 1.99*y[i+1] - y[i]
    x = x + 1
    return x, y

x, y = func()
plt.scatter(x,y)
plt.plot(x,y)
plt.grid()
plt.show()
