# 16-4. Automatic Indexes: In this section, we hardcoded the indexes correspond-
# ing to the TMIN and TMAX columns. Use the header row to determine the indexes
# for these values, so your program can work for Sitka or Death Valley. Use the sta-
# tion name to automatically generate an appropriate title for your graph as well.

from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

def load(path, name_idx, date_idx,high_idx,low_idx):
    path = Path(path)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Extract dates, and high and low temperatures.
    name = ''
    dates, highs, lows = [], [], []
    for row in reader:
        name = row[name_idx]
        current_date = datetime.strptime(row[date_idx], '%Y-%m-%d')
        try:
            high = int(row[high_idx])
            low = int(row[low_idx])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return (name, dates,highs,lows)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')

(name, dates,highs,lows) = load('weather_data/death_valley_2021_simple.csv',1, 2,3,4)

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily High and Low Temperatures, 2021\n{name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

plt.show()
