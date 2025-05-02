# 15-6. Two D8s: Create a simulation showing what happens when you roll two
# eight-sided dice 1,000 times. Try to picture what you think the visualization will
# look like before you run the simulation, then see if your intuition was correct.
# Gradually increase the number of rolls until you start to see the limits of your
# system’s capabilities.

import plotly.express as px

from die import Die

# Create a D6.
die = Die(8)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()+die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(2, die.num_sides*2+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling Two D8 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
