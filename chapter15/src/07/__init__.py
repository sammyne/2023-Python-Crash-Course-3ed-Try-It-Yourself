# 15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll
# is 3 and the largest number is 18. Create a visualization that shows what hap-
# pens when you roll three D6 dice.

import plotly.express as px

from die import Die

# Create a D6.
die = Die(6)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()+die.roll()+die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(3, die.num_sides*3)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling Three D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
