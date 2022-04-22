#!/usr/bin/python3

import matplotlib.pyplot as plt

x_axis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis1 = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]

x_axis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis2 = [53, 6, 46, 36, 15, 64, 73, 25, 82, 9]

plt.title("Prices over 10 years")

plt.scatter(x_axis1, y_axis1, color='darkblue', marker='x', label="item 1")
plt.scatter(x_axis2, y_axis2, color='darkred', marker='x', label="item 2")

plt.xlabel("Time (years)")
plt.ylabel("Price (dollars)")

plt.grid(True)
plt.legend()

plt.show()