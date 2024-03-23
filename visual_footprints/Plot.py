import matplotlib.pyplot as plt
import numpy as np

#File formate: Name latitude(y) longitude(x)
New_file = open("Nodes_graph.txt", "r")
img = plt.imread("Map.png")
x = []
y = []

for i in New_file:
    z = i.split()
    x.append(float(z[2]))
    y.append(float(z[1]))
fig, ax = plt.subplots()
ax.imshow(img, extent=[-123.7939, -119.3994, 37.2653, 41.5086])
plt.scatter(np.array(x), np.array(y))
plt.show()

print("Done")

