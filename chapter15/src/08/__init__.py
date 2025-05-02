# 15-8. Multiplication: When you roll two dice, you usually add the two numbers
# together to get the result. Create a visualization that shows what happens if you
# multiply these numbers by each other instead.

import plotly.express as px

from die import Die

# Create a D6.
die = Die(6)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()*die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides**2)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
