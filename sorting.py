# Sort netflix_data by descending release_year
netflix_data_year = netflix_data.sort_values('release_year',ascending=False)

print(netflix_data_year)
