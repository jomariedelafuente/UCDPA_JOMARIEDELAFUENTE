import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")

# Sort tv_shows by rotten_tomatoes
tv_shows_rotten_tomatoes = tv_shows.sort_values('Rotten Tomatoes',ascending=False)

# Print the top few rows
print(tv_shows_rotten_tomatoes)

# Sort the index of tv_shows_ind
tv_shows_srt = tv_shows.sort_index()
