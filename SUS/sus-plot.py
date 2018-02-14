import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys

infile1 = sys.argv[1]
tool = "Title1"
metric_title = "SUS"

#infile1 = 'sus-results-tool1.csv'

# Load data from csv file into NumPy dataframe
data1 = pd.read_csv(infile1, sep=',', na_values='.')

# Get mean and std
data1['total'].mean()
data1['total'].std()
data1['total'].median()

# Test the loaded data in Python
loaded_data = data1.iloc[:,[1]]
loaded_data

## Add the collection into a list
data_to_plot = [loaded_data]

# Create the boxplot

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
# Notched boxplot
#bp = ax.boxplot(data_to_plot, notch=1, patch_artist=1, sym='+', vert=1, whis=1.5)
#Standard boxplot
bp = ax.boxplot(data_to_plot, notch=0, patch_artist=1, sym='+', vert=1, whis=1.5)

# Add a horizontal grid to the plot, but make it very light in color
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax.set_axisbelow(True)
ax.set_title(metric_title)
ax.set_xlabel('Tool')
ax.set_ylabel('Value')

## Custom x-axis labels
ax.set_xticklabels([tool])

ax.set_ylim(0, 100)

# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')

plt.show()
