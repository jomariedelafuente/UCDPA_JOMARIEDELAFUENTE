import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")


tv_shows.drop(["Unnamed: 0",'type'],axis=1,inplace=True)

tv_shows.dropna(inplace=True)

print(tv_shows.drop)

# Find the shape of an array
print(tv_shows.shape)

# Print the column names of data
print(tv_shows.columns)

# Sort tv_shows by year
tv_shows_year = tv_shows.sort_values('Year',ascending=False)

# Print the top few rows
print(tv_shows_rotten_tomatoes)

# Sort the index of tv_shows_ind
tv_shows_srt = tv_shows.sort_index()
