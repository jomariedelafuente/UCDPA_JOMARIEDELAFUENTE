import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")
# Print the column names of data
print(tv_shows.columns)

tv_shows.drop(["Unnamed: 0",'type'],axis=1,inplace=True)

tv_shows.dropna(inplace=True)

print(tv_shows.drop)

# Print the column names of data
print(tv_shows.columns)