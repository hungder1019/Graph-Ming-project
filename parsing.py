import csv
import networkx as nx

G = nx.Graph()
csvFileNames = ['data/T3_Water_Mercury.csv', 'data/T4_Sediment_Mercury.csv', 'data/T5_Invertebrates_Mercury.csv',
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

for n in G.nodes():
    print(n)
    for table in G.nodes[n]:
        print(table)
        for category in G.nodes[n][table]:
            helperStr = category + ': '
            for c in G.nodes[n][table][category]:
                helperStr += c + ", "
            print(helperStr)
        print('')
    break