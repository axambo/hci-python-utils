import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
infile3 = sys.argv[3]

tool1 = "Title1"
tool2 = "Title2"
tool3 = "Title3"

#infile1 = 'sus-results-tool1.csv'
#infile2 = 'sus-results-tool2.csv'
#infile3 = 'sus-results-tool3.csv'

# Load data from csv file into NumPy dataframe
data1 = pd.read_csv(infile1, sep=',', na_values='.')
data2 = pd.read_csv(infile2, sep=',', na_values='.')
data3 = pd.read_csv(infile3, sep=',', na_values='.')

# Get mean and std
data1['total'].mean()
data1['total'].std()
data1['total'].median()
data2['total'].mean()
data2['total'].std()
data2['total'].median()
data3['total'].mean()
data3['total'].std()
data3['total'].median()

# Test the loaded data in Python
tool1_data = data1.iloc[:,[1]]
tool2_data = data2.iloc[:,[1]]
tool3_data = data3.iloc[:,[1]]
tool1_data

## Combine these different collections into a list
data_to_plot = [tool1_data, tool2_data, tool3_data]

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
ax.set_title('Comparison of sus Across Three Tools')
ax.set_xlabel('Tool')
ax.set_ylabel('Value')

## Custom x-axis labels
ax.set_xticklabels([tool1, tool2, tool3])

ax.set_ylim(0, 100)

## Remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Save the figure
fig.savefig('multiple-boxplot.png', bbox_inches='tight')

plt.show()
