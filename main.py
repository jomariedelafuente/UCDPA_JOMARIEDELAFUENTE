import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',11)

# data set is called = tv_shows
tv_shows = pd.read_csv('tv_shows.csv')

# print the dataset
print(tv_shows.head)

# Print the column names of data
print(tv_shows.columns)

# removing in unnamed index column
tv_shows=tv_shows.iloc[:,1:]

# print the updated dataset
print(tv_shows)
print(tv_shows.columns)

# Remove "Type" column - not relevant
tv_shows.drop(['type'],axis=1,inplace=True)

print(tv_shows.drop)

# Find columns that had missing values
print(tv_shows.isnull().any())

# Find how many values were missing in each columns
print(tv_shows.isnull().sum())



# Find if columns still have missing values
print(tv_shows.isnull().any())

# Sort tv_shows by IMDb
tv_shows_IMDb = tv_shows.sort_values(by="IMDb", ascending=False)

# print the top 10 tv show ratings
print(tv_shows_IMDb.head(10))

print(tv_shows.describe())

# Sort tv_shows by year
tv_shows_year = tv_shows.sort_values('Year',ascending=True)

# Print the top 10 tv shows
print(tv_shows_year.head(10))

print(tv_shows.sum())

tv_shows_total = tv_shows.groupby('Age')['Netflix'].sum()
print(tv_shows_total)

tv_shows_total.plot(kind='bar')

# Show the plot
plt.show()
