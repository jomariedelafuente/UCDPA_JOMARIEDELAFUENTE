import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from prettytable import PrettyTable

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

# Remove "Type" column - not relevant
tv_shows.drop(['Rotten Tomatoes'],axis=1,inplace=True)

print(tv_shows.columns)

# Summary of statistics on the dataframe
print(tv_shows.describe())



# Find total TV shows available on each streaming platform
tv_shows_sum = tv_shows.sum()["Netflix":"Disney+"]
print(tv_shows_sum)

height = [1931, 1754, 2144, 180, ]
bars = ('Netflix', 'Hulu', 'Prime Video', 'Disney+')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height)

# use the plt.xticks function to custom labels
plt.xticks(y_pos, bars, color='Green', rotation=0, fontweight='bold', fontsize='10', horizontalalignment='center')

# remove labels
plt.tick_params(labelbottom='off')
plt.title("Number of TV Shows Available On Each Platform")

plt.show()

# Plot the years in which the TV Shows on Netflix was produced
tv_shows_by_year= tv_shows.groupby(['Year'])[['Netflix','Hulu','Prime Video','Disney+']].sum()

# Create a line plot of the years in which the TV Shows on each platform was produced
tv_shows_by_year.plot(kind='bar')
tv_shows_by_year.plot(title='Number of TV Shows Produced from 1901 to 2020')

# Show the plot
plt.show()

# Sort tv_shows by IMDb
tv_shows_IMDb = tv_shows.sort_values(by="IMDb", ascending=False)

# print the top 5 tv show ratings
print(tv_shows_IMDb.head(5))

from prettytable import PrettyTable

# Print the top 5 TV Show Ratings in a table
tv_shows_IMDb = PrettyTable(['Top 5','Title', 'Year','IMDb','Platform'])
tv_shows_IMDb.add_row(['1','Destiny', 2014, 9.6, 'Hulu'])
tv_shows_IMDb.add_row(['2','Breaking Bad', 2008,9.5, 'Netflix'])
tv_shows_IMDb.add_row(['3','Malgudi Days', 1987,9.5,'Prime_Video'])
tv_shows_IMDb.add_row(['4','Hungry Henry', 2014,9.5, 'Hulu'])
tv_shows_IMDb.add_row(['5','Band of Brothers', 2001,9.4, 'Prime_Video'])

print(tv_shows_IMDb)

# Sort tv_shows by year
tv_shows_year = tv_shows.sort_values('Year',ascending=True)

# Print the top 5 tv shows
print(tv_shows_year.head(5))

from prettytable import PrettyTable
# Print the top 5 oldest TV Shows in a table
tv_shows_oldest = PrettyTable(['Top 5 Oldest Shows','Title', 'Year','Platform'])
tv_shows_oldest.add_row(['1','Gods & Monsters with Tony Robinson', 1901, 'Prime_Video'])
tv_shows_oldest.add_row(['2','Space: The New Frontier Bad', 1901, 'Prime_Video'])
tv_shows_oldest.add_row(['3','History of Westinghouse ', 1904, 'Prime_Video'])
tv_shows_oldest.add_row(['4',' Born To Explore ', 1914, 'Netflix'])
tv_shows_oldest.add_row(['5','The Little Rascals Classics', 1931, 'Hulu'])

print(tv_shows_oldest)


# TV Shows Target Age Group For Each Platform
tv_shows_by_Age= tv_shows.groupby(['Age'])[['Netflix','Hulu','Prime Video','Disney+']].sum()

# Create a line plot of the years in which the TV Shows on Netflix was produced
tv_shows_by_Age.plot(kind='bar')
tv_shows_by_Age.plot(title='TV Shows Target Age Group For Each Platform')

# Show the plot
plt.show()



