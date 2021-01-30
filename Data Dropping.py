import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")
# Print the column names of data
print(tv_shows.columns)

tv_shows.drop(["Unnamed: 0",'type'],axis=1,inplace=True)

print(tv_shows.drop)

# Print the column names of data
print(tv_shows.columns)

print(tv_shows.isnull().any())


print(tv_shows.info())

print(tv_shows.describe())