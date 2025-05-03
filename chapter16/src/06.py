# 16-6. Refactoring: The loop that pulls data from all_eq_dicts uses variables for
# the magnitude, longitude, latitude, and title of each earthquake before append-
# ing these values to their appropriate lists. This approach was chosen for clarity
# in how to pull data from a GeoJSON file, but it’s not necessary in your code.
# Instead of using these temporary variables, pull each value from eq_dict and
# append it to the appropriate list in one line. Doing so should shorten the body
# of this loop to just four lines.

from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)
# Create a more readable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])

print(mags[:10])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=titles)
fig.show()
