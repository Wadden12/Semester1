Xaxis1 = []
Yaxis1 = []
Xaxis2 = []
Yaxis2 = []
from math import sqrt

for x in range(-100, 101):
    y = 2 * x ** 2 + 4 * x - 5
    Xaxis1.append(x)
    Yaxis1.append(y)
    Xaxis2.append(x)
    y2 = (5 * x + 3) ** 2
    Yaxis2.append(y2)

#!/usr/bin/python3

import matplotlib.pyplot as plt

plt.title("Lesson 30 Quesiton 1")

plt.plot(Xaxis1, Yaxis1, color='darkblue', label="item 1")
plt.plot(Xaxis2, Yaxis2, color='darkred',  label="item 2")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.legend()

plt.show()

