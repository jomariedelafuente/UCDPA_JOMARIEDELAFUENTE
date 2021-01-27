import matplotlib.pyplot as plt
fig,ax = plt.subplots()
plt.show()
import pandas as pd

tv_shows = pd.read_csv("tv_shows.csv")

x = data['year'].head(5)
y1 = data['netflix'].head(5)
y2 = data['disney'].head(5)

ax.plot(x,y1)
ax.plot(x,y2)