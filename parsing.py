import csv
import networkx as nx
import os
import matplotlib.pyplot as plt
import numpy as np
from math import *

def haversine(lon1, lat1, lon2, lat2):
    
    # Calculate the great circle distance in kilometers between two points 
    # on the earth (specified in decimal degrees)
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

G = nx.Graph()
csvFileNames = ['data/T2_Study_Sites.csv', 'data/T3_Water_Mercury.csv', 'data/T4_Sediment_Mercury.csv', 'data/T5_Invertebrates_Mercury.csv',
                 'data/T6_Frogs_Mercury.csv', 'data/T7_Fish_Mercury.csv', 'data/T8_Water_FieldParameters.csv',
                 'data/T9_Water_Isotopes_Nutrients_MajorIons.csv', 'data/T10_Water_TraceElements_Filtered.csv',
                 'data/T11_Water_TraceElements_Unfiltered.csv', 'data/T12_Sediment_TraceElements.csv',
                 'data/T13_Invertebrates_TraceElements.csv', 'data/T14_Fish_TraceElements.csv',
                 'data/T15_GeometricMean_MercuryConcentrations.csv', 'data/T16_Normalized_Mercury_Values.csv']

stationCSV = 'data/T2_Study_Sites.csv'
with open(stationCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    counter = 0
    for row in csvreader:
        if(counter != 0):
            G.add_node(row[0])
        counter += 1


for file_name in csvFileNames:
    csv_file_path = file_name

    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        rowCtr = 0
        categories = []
        prevRowZero = ''
        for row in csvreader:
            if(rowCtr == 0):
                ignoreStationIdFlag = 0
                for r in row:
                    if(ignoreStationIdFlag != 0):
                        categories.append(r)
                    ignoreStationIdFlag = 1
            if(row[0] != prevRowZero and rowCtr != 0):
                if(row[0] != ''):
                    G.nodes[row[0]][csv_file_path] = {}
                    for c in categories:
                        G.nodes[row[0]][csv_file_path][c] = []
            if(rowCtr != 0):
                rowLoc = 0
                for r in row:
                    if(rowLoc != 0):
                        if(row[0] != ''):
                            G.nodes[row[0]][csv_file_path][categories[rowLoc-1]].append(r)
                    rowLoc += 1
            rowCtr += 1
            prevRowZero = row[0]


###TEST PRINTING###
# for n in G.nodes():
#     print(n)
#     for table in G.nodes[n]:
#         print(table)
#         for category in G.nodes[n][table]:
#             helperStr = category + ': '
#             for c in G.nodes[n][table][category]:
#                 helperStr += c + ", "
#             print(helperStr)
#         print('')
#     break

###MAP COLORING###
# here = os.path.dirname(os.path.abspath(__file__))
# img = plt.imread(os.path.join(here, 'visual_footprints/Map.png'))

# latitude = []
# longitude = []
# colorVars = []
# for n in G.nodes():
#     colorVarTemp = G.nodes[n]['data/T15_GeometricMean_MercuryConcentrations.csv']['Geometric Mean Water Mercury Unfiltered (ng/L)'][0]
#     if(colorVarTemp == 'ND'): continue
#     else:
#         latitude.append(float(G.nodes[n]['data/T2_Study_Sites.csv']['Latitude'][0]))
#         longitude.append(float(G.nodes[n]['data/T2_Study_Sites.csv']['Longitude'][0]))
#         colorVars.append(float(colorVarTemp))


# fig, ax = plt.subplots()
# ax.imshow(img, extent=[-123.7939, -119.3994, 37.2653, 41.5086])
# #note: latitude(y) longitude(x)

# for c in colorVars:
#     print(c)

# plt.scatter(np.array(longitude), np.array(latitude), s=5, c = np.array(colorVars), cmap = "Blues")
# plt.show()

###ADDITION OF "SCORE SITES" AND EDGE CREATION FOR BIPARTITE STRUCTURE###
mineNodes = set(G.nodes())
scoreSites = []
with open('data/T0_City_Sites.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    rowCtr = 0
    for row in csvreader:
        if(rowCtr != 0 and row[0] != ''):
            G.add_node(row[0])
            scoreSites.append(row[0])
            G.nodes[row[0]]['Latitude'] = float(row[1])
            G.nodes[row[0]]['Longitude'] = float(row[2])
            G.nodes[row[0]]['Elevation'] = float(row[3])
            for n in mineNodes:
                curLat = float(G.nodes[n]['data/T2_Study_Sites.csv']['Latitude'][0])
                curLong = float(G.nodes[n]['data/T2_Study_Sites.csv']['Longitude'][0])
                distance = haversine(G.nodes[row[0]]['Longitude'], G.nodes[row[0]]['Latitude'], curLong, curLat)
                G.nodes[row[0]][n] = distance
        rowCtr += 1

keyList = ['Geometric Mean Water Mercury Unfiltered (ng/L)', 'Geometric Mean Water Mercury Filtered (ng/L)',
            'Geometric Mean Water Methylmercury Unfiltered (ng/L)', 'Geometric Mean Water Methylmercury Filtered (ng/L)']

for site in scoreSites:
    distSum = 0.0
    mercValSum = 0.0
    siteElev = G.nodes[site]['Elevation']
    for m in mineNodes:
        mineElev = float(G.nodes[m]['data/T2_Study_Sites.csv']['Elevation'][0])
        distSum += G.nodes[site][m]
        for k in keyList:
            if(G.nodes[m]['data/T15_GeometricMean_MercuryConcentrations.csv'][k][0] != ''):
                modifier = 1.0
                rawVal = float(G.nodes[m]['data/T15_GeometricMean_MercuryConcentrations.csv'][k][0])
                if(siteElev < mineElev): modifier += 0.25
                else: modifier -= 0.25
                mercValSum += rawVal * modifier
    else: 
        s = 1
        G.nodes[site]['score'] = (log(s * mercValSum/distSum)) * 4
    print(site + ": " + str(G.nodes[site]['score']))

here = os.path.dirname(os.path.abspath(__file__))
img = plt.imread(os.path.join(here, 'visual_footprints/New_Map.png'))
latitudes = []
longitudes = []
colorVars = []
for site in scoreSites:
    latitudes.append(G.nodes[site]['Latitude'])
    longitudes.append(G.nodes[site]['Longitude'])
    colorVars.append(G.nodes[site]['score'])
print(colorVars)
min_color = min(colorVars) if min(colorVars) >= 0 else min(colorVars) * -1
score_cp = []
for i in colorVars:
    score_cp.append(i + min_color + 2.7)
lat_c = []
lon_c = []
for i in latitudes:
    lat_c.append(i)
for i in longitudes:
    lon_c.append(i)
#Mines
New_file = open(os.path.join(here, "visual_footprints/Nodes_graph.txt"), "r")
x = []
y = []
scale = min(score_cp)
s2 = [45 for n in range(len(longitudes))]
print(scale)
print(score_cp)

c2 = [[(scale/score), (scale/score), (scale/score)] for score in score_cp]
for i in New_file:
    z = i.split()
    x.append(float(z[2]))
    y.append(float(z[1]))
longitudes += x
latitudes += y
s1 = [15 for n in range(len(x))]
c1 = [[0, 0, 1.0] for n in range(len(x))]
s2 += s1
c2 += c1

#text
text = [round(n, 2) for n in colorVars]
text1 = [""*len(x)]
text += text1

fig, ax = plt.subplots()
ax.imshow(img, extent=[-123.7939, -118, 36, 41.5086])
plt.scatter(np.array(longitudes), np.array(latitudes), s = np.array(s2), c = (np.array(c2)/1.0), edgecolors='black', linewidths=.5)
plt.title("Score of chosen area in relation of distancce")
plt.xlabel("Longitudes")
plt.ylabel("Latitudes")
for i in range(len(text)):
    plt.text(longitudes[i], latitudes[i], text[i], color = "red")
plt.show()


elevation_file = open(os.path.join(here, "elevation.txt"), "r")
elevation = [float(i) for i in elevation_file]
city_file = open(os.path.join(here, "city_elevation.txt"), "r")
city_elevation = [float(i) for i in city_file]
total_elevation = city_elevation + elevation

#plt.clf()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for shape, ele, lo, la in [('o', elevation, x, y), ('^', city_elevation, lon_c, lat_c)]:
    xs = lo
    ys = la
    zs = ele
    print(len(xs))
    print(len(ys))
    print(len(zs))
    ax.scatter(xs, ys, zs, marker=shape)
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
ax.set_zlabel('elevation (m) above sea')
plt.show()