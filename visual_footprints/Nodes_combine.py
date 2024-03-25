


a = open("Nodes_name.txt", "r")
b = open("Nodes_latitude.txt", "r")
c = open("Nodes_longitude.txt", "r")

New_file = open("Nodes_graph.txt", "w")
for i in range(251):
    New_file.write(a.readline().strip('\n') + " " + b.readline().strip('\n') + " " + c.readline())

print("Done")