# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

x = range(1, 5000)
y = [v**3 for v in x]

# print(plt.style.available)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()
