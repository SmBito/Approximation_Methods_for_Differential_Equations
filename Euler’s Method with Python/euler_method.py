import numpy as np
from matplotlib import pyplot as plt

x0 = 0
y0 = 1
xf = 10
n = 101
deltax = (xf - x0)/(n-1)

x = np.linspace(x0, xf, n)
y = np.zeros([n])

y[0] = y0

for i in range(1, n):
    y[i] = deltax * (- y[i-1] + np.sin(x[i-1])) + y[i-1]

for i in range(n):
    print(x[i], y[i])

plt.plot(x, y, 'o')
plt.xlabel("value of x")
plt.ylabel("value of y")
plt.title("Approximate Solution with Forward Euler’s Method")
plt.show( )