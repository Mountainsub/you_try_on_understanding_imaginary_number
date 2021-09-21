import numpy as np
from matplotlib import pyplot as plt
def func():
    size = 10
    x = np.arrange(size)
    y = np.zeros(size)
    y[0] = 1
    y[1] = 5
    for i in range(size-2):
        y[i+2] = 5*y[i+1] - 6*y[i]
    x = x + 1
    return x, y

x, y = func()
plt.scatter(x,y)
plt.plot(x,y)
plt.grid()
plt.show()
