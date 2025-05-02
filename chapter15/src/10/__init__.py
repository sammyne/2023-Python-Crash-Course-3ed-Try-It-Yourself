# 15-10. Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
# visualization, and use Plotly to make the visualization for a random walk. (You’ll
# need to consult the documentation for each library to complete this exercise.)

import matplotlib.pyplot as plt
import plotly.express as px

from die import Die
from random_walk import RandomWalk

# Create a D6.
die = Die(6)
# Make some rolls, and store results in a list.
results = [die.roll()+die.roll() for i in range(1000)]

# Analyze the results.
poss_results = range(1*2, die.num_sides*2)
frequencies = [results.count(v) for v in poss_results]

plt.bar(poss_results, frequencies)
plt.title('Results of Rolling Two D6 1,000 Times')
plt.show()

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()
# Plot the points in the walk.
fig = px.scatter(rw.x_values, rw.y_values)
fig.show()

# fig, ax = plt.subplots(figsize=(15, 9))
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
# ax.set_aspect('equal')
