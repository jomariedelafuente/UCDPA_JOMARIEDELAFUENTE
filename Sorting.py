import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")

# Sort tv_shows by year
tv_shows_year = tv_shows.sort_values('Year',ascending=False)

# Print the top few rows
print(tv_shows_year)

