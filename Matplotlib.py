import matplotlib.pyplot as plt

import pandas as pd

# data set is called = tv_shows

# Basic plot
import numpy as np
import matplotlib.pyplot as plt

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







