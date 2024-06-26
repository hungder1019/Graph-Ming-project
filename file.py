import pandas as pd
import networkx as nx

df1 = pd.read_csv("./data/T1_Data_Dictionary.csv")
df2 = pd.read_csv("./data/T2_Study_Sites.csv")
df3 = pd.read_csv("./data/T3_Water_Mercury.csv")
df4 = pd.read_csv("./data/T4_Sediment_Mercury.csv")
df5 = pd.read_csv("./data/T5_Invertebrates_Mercury.csv")
df6 = pd.read_csv("./data/T6_Frogs_Mercury.csv")
df7 = pd.read_csv("./data/T7_Fish_Mercury.csv")
df8 = pd.read_csv("./data/T8_Water_FieldParameters.csv")
df9 = pd.read_csv(
    "./data/T9_Water_Isotopes_Nutrients_MajorIons.csv")  # Edited
df10 = pd.read_csv("./data/T10_Water_TraceElements_Filtered.csv")
df11 = pd.read_csv("./data/T11_Water_TraceElements_Unfiltered.csv")
df12 = pd.read_csv("./data/T12_Sediment_TraceElements.csv")
df13 = pd.read_csv("./data/T13_Invertebrates_TraceElements.csv")
df14 = pd.read_csv("./data/T14_Fish_TraceElements.csv")
df15 = pd.read_csv("./data/T15_GeometricMean_MercuryConcentrations.csv")
df16 = pd.read_csv("./data/T16_Normalized_Mercury_Values.csv")
df_sigma = [df1, df2, df3, df4, df5, df6, df7, df8,
            df9, df10, df11, df12, df13, df14, df15, df16]

print("df1")
print(df1)
print("df2")
print(df2)
print("df3")
print(df3)
print("df4")
print(df4)
print("df5")
print(df5)
print("df6")
print(df6)
print("df7")
print(df7)
print("df8")
print(df8)
print("df9")
print(df9)
print("df10")
print(df10)
print("df11")
print(df11)
print("df12")
print(df12)
print("df13")
print(df13)
print("df14")
print(df14)
print("df15")
print(df15)
print("df16")
print(df16)
