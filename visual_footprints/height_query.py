import requests
import urllib
import pandas as pd
import os
# little progress bar im testing with
from tqdm import tqdm

# This code makes requests to:
# USGS Elevation Point Query Service
# with longitude and latitude to find height
# that data will then be placesd in a txt file to be read by parsing_w_elevation.py

# might take a while
url = r'https://epqs.nationalmap.gov/v1/json?'

# abs file path
here = os.path.dirname(os.path.abspath(__file__))
lat_file = open(os.path.join(here, "Nodes_latitude.txt"), "r")
lon_file = open(os.path.join(here, "Nodes_longitude.txt"), "r")
# insert data
lat = [float(i.strip("\n")) for i in lat_file]
lon = [float(i.strip("\n")) for i in lon_file]

# create data frame
df = pd.DataFrame({
    'lat': lat,
    'lon': lon
})


elevations = []
for lat, lon in tqdm(zip(df['lat'], df['lon'])):
    # define query params
    params = {
        'output': 'json',
        'x': lon,
        'y': lat,
        'units': 'Meters'
    }
    # query value
    result = requests.get((url + urllib.parse.urlencode(params)))
    elevations.append(result.json()['value'])

df['elev_meters'] = elevations
print(df)

New_file = open("elevation.txt", "w")
tbd = df['elev_meters']
for i in tbd:
    New_file.write(i + "\n")

print("done")