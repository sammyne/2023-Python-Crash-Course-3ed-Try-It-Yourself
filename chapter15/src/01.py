# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5,000 cubic numbers.

import matplotlib.pyplot as plt

x = range(1, 5000)
y = [v**3 for v in x]

# print(plt.style.available)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x, y, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()
