import pandas as pd
import sys

infile = sys.argv[1]
outfile = sys.argv[2]
# infile = 'sus-input-data.csv'
# outfile = 'sus-results-tool1.csv'


# Load data from csv file
data = pd.DataFrame.from_csv(infile)

# Test the loaded data in Python
data

# Create a list to store the data
sus = []

# For each row in the column,
for index, row in data.iterrows() :
    odd = (row['Q1'] + row['Q3'] + row['Q5'] + row['Q7'] + row['Q9']) - 5
    even = 25 - (row['Q2'] + row['Q4'] + row['Q6'] + row['Q8'] + row['Q10'])
    total = (odd + even) * 2.5
    sus.append(total)
    print(total)

# Create a column from the list
data['total'] = sus

# Write results to a csv file
data['total'].to_csv(outfile, header=["total"])
