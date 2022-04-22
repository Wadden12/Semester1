X_Axis = []
Y_Axis = []

for x in range(-100, 101):
    X_Axis.append(x)
    y = 3 * x - 4
    Y_Axis.append(y)

#!/usr/bin/python3

import matplotlib.pyplot as plt

plt.title("Lesson 30 Quesiton 1")

plt.scatter(X_Axis, Y_Axis, color='teal', marker='x', label="item 1")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.legend()

plt.show()




