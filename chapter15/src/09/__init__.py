# 15-9. Die Comprehensions: For clarity, the listings in this section use the long
# form of for loops. If you’re comfortable using list comprehensions, try writing a
# comprehension for one or both of the loops in each of these programs.

import plotly.express as px

from die import Die

# Create a D6.
die = Die(6)
# Make some rolls, and store results in a list.
results = [die.roll()*die.roll() for i in range(1000)]

# Analyze the results.
poss_results = range(1, die.num_sides**2)
frequencies = [results.count(v) for v in poss_results]

title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
