import csv
import networkx as nx

G = nx.Graph()
csvFileNames = ['data/T3_Water_Mercury.csv', 'data/T4_Sediment_Mercury.csv', 'data/T5_Invertabrates_Mercury.csv',
                 'data/T6_Frogs_Mercury.csv', 'data/T7_Fish_Mercury.csv', 'data/T8_Water_FieldParameters.csv']

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

        flag = 0
        categories = []
        for row in csvreader:
            if(flag == 0):
                flag = 1
                ignoreStationIdFlag = 0
                for r in row:
                    if(ignoreStationIdFlag != 0):
                        categories.append(r)
                    ignoreStationIdFlag = 1
            else:
                for c in categories:
                    G.nodes[row[0]][c] = []

        for row in csvreader:
            rowLoc = 1
            for r in row:
                G.nodes[row[0]][categories[rowLoc]].append(r)
                rowLoc += 1
            