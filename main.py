import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")
print(tv_shows)

# Find the shape of an array
print(tv_shows.shape)


# Print the column names of data
print(tv_shows.columns)

# Find how many unique
print(tv_shows.nunique())

print(tv_shows.duplicated().sum())

