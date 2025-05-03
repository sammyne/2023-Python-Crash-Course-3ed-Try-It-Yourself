# 16-1. Sitka Rainfall: Sitka is located in a temperate rainforest, so it gets a fair
# amount of rainfall. In the data file sitka_weather_2021_full.csv is a header called
# PRCP, which represents daily rainfall amounts. Make a visualization focusing on
# the data in this column. You can repeat the exercise for Death Valley if you’re
# curious how little rainfall occurs in a desert.

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# Extract dates and high temperatures.
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    prcp = float(row[5])
    dates.append(current_date)
    prcps.append(prcp)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='red')

# Format plot.
ax.set_title("Daily PRCP, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()

ax.set_ylabel("PRCP", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
