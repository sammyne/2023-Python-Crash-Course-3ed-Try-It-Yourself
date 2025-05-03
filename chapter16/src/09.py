# 16-9. World Fires: In the resources for this chapter, you’ll find a file called
# world_fires_1_day.csv. This file contains information about fires burning in differ-
# ent locations around the globe, including the latitude, longitude, and brightness
# of each fire. Using the data-processing work from the first part of this chapter
# and the mapping work from this section, make a map that shows which parts of
# the world are affected by fires.
# You can download more recent versions of this data at https://earthdata
# .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data. You can
# find links to the data in CSV format in the SHP, KML, and TXT Files section.

from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

latitudes, longitudes, brightness = [], [], []
for row in reader:
    latitudes.append(float(row[0]))
    longitudes.append(float(row[1]))
    brightness.append(float(row[2]))

TITLE = 'World Fires'

fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightness, title=TITLE,
    color=brightness,
    color_continuous_scale='Viridis',
    labels={'color':'Brightness'},
    projection='natural earth')
fig.show()
