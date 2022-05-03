import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# creating space
fig = plt.figure()
ax = plt.subplot()

#true value of integral
integral = -4

#segment start and finish points
a = -2
b = 0

# segment length
length = abs(b - a)

# given function
def f(x):
    return x**3

# function for drawing integral sums
def draw_integral_sums(n, type):
    s = 0
    if type == 1:
        for i in range(0, n):
            xk = a+length*i/n
            s += length/n * f(xk)
            ax.add_patch(Rectangle((xk, 0), length/n, f(xk)))
    if type == 2:
        for i in range(0, n):
            xk = a+length*i/n
            s += length / n * f((2*xk + length/n) / 2)
            ax.add_patch(Rectangle((xk, 0), length/n, f((2*xk + length/n) / 2)))
    if type == 3:
        for i in range(0, n):
            xk = a+length*i/n
            s += length / n * f(xk + length/n)
            ax.add_patch(Rectangle((xk, 0), length/n, f(xk + length/n)))
    print("Square: " + str(s))
    print("Infelicity: " + str(abs(s - integral)))

#data for function
x_data = np.arange(a, b, 0.01)
y_data = f(x_data)

#drawing function
ax.plot(x_data, y_data, color='orange')
draw_integral_sums(100, 3)

ax.legend(["Функция", "Интегральная сумма"])
ax.set_ylabel("Y")
ax.set_xlabel("X")
#ax.plot([-2, 0], [0, 0], '--', color='black')
#ax.plot([0, 0], [-8, 0], '--', color='black')
ax.grid(which='major')
ax.minorticks_on()
ax.grid(which='minor',
        color='black',
        linestyle=':')

plt.show()