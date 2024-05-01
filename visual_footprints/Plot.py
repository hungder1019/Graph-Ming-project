import matplotlib.pyplot as plt
import numpy as np
import os

here = os.path.dirname(os.path.abspath(__file__))

#File formate: Name latitude(y) longitude(x)
New_file = open(os.path.join(here, "Nodes_graph.txt"), "r")
img = plt.imread(os.path.join(here, "New_Map.png"))
x = []
y = []

for i in New_file:
    z = i.split()
    x.append(float(z[2]))
    y.append(float(z[1]))
fig, ax = plt.subplots()
ax.imshow(img, extent=[-123.7939, -118, 36, 41.5086])
plt.scatter(np.array(x), np.array(y))
plt.show()

print("Done")

