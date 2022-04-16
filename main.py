import pandas as pd 
import csv 

df = pd.read_csv("allthestars.csv")
print(df.shape)

del df["Luminosity"]
del df["Mass"]
del df["Star_name"]
del df["Distance"]
del df["Radius"]

df = df.rename({
    'Star_name': "name_of_star"
}, axis='columns')

print(df.shape)
df.to_csv('main.csv')