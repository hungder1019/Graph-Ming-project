import csv
import networkx as nx

G = nx.Graph()
csvFileNames = ['placeholder1', 'placeholder2']

for file_name in csvFileNames:
    csv_file_path = file_name

    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if(not G.hasNode(row[1])):
               
        