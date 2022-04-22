#!/usr/bin/python3

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [46, 38, 29, 22, 13, 11]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Olympic Gold medals in London')
ax.set_ylabel('Gold medals')
ax.set_xlabel('Countries')

ax.set_xticks(x)
ax.set_xticklabels(("USA", "China", "UK", "Russia",
    "South Korea", "Germany"))

plt.show()