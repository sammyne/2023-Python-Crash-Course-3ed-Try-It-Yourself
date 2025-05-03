# 16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and
# Death Valley graphs reflect the different data ranges. To accurately compare
# the temperature range in Sitka to that of Death Valley, you need identical scales
# on the y-axis. Change the settings for the y-axis on one or both of the charts in
# Figures 16-5 and 16-6. Then make a direct comparison between temperature
# ranges in Sitka and Death Valley (or any two places you want to compare).

from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

def load(path, date_idx,high_idx,low_idx):
    path = Path(path)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Extract dates, and high and low temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
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

    return (dates,highs,lows)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')

(dates,highs,lows) = load('weather_data/death_valley_2021_simple.csv', 2,3,4)

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


(dates,highs,lows) = load('weather_data/sitka_weather_2021_simple.csv', 2,4,5)
ax.plot(dates, highs, color='black', alpha=0.5)
ax.plot(dates, lows, color='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA vs Sitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)


plt.show()
