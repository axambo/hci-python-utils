import pandas as pd
import numpy
import sys
import csv

# function from: http://www.idiotinside.com/2015/04/14/export-dict-to-csv-list-to-csv-in-python/
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

# Load data from csv file
#factordata = sys.argv[1]
#pairwisedata = sys.argv[2]
#outputdata = sys.argv[3]
#outputfactordata = sys.argv[4]
#outputfactordata_sorted = sys.argv[5]
factordata = pd.DataFrame.from_csv('csi-input-factor-data.csv')
pairwisedata = pd.DataFrame.from_csv('csi-input-pairwise-data.csv')
outputdata = 'csi-results.csv'
outputfactordata = 'csi-factors-results.csv'
outputfactordata_sorted = 'csi-factors-results-sorted.csv'

CSIScore = []
CSIScoreByFactors = []

# Test the loaded data in Python
factordata

# PART1

# Create a list to store the data
csi_collab_average = []
csi_enjoy_average = []
csi_expl_average = []
csi_expr_average = []
csi_immer_average = []
csi_effor_average = []

# For each row in the column,
for index, row in factordata.iterrows() :
    Collaboration_Average = (float(row['Collaboration1']) + float(row['Collaboration2']))/2
    Enjoyment_Average = (float(row['Enjoyment1']) + float(row['Enjoyment2']))/2
    Exploration_Average = (float(row['Exploration1'] + row['Exploration2']))/2
    Expressiveness_Average = (float(row['Expressiveness1'] + row['Expressiveness2']))/2
    Immersion_Average = (float(row['Immersion1'] + row['Immersion2']))/2
    ResultsWorthEffort_Average = (float(row['ResultsWorthEffort1'] + row['ResultsWorthEffort2']))/2
    # Store each average set of values per participant in a list
    csi_collab_average.append(Collaboration_Average)
    csi_enjoy_average.append(Enjoyment_Average)
    csi_expl_average.append(Exploration_Average)
    csi_expr_average.append(Expressiveness_Average)
    csi_immer_average.append(Immersion_Average)
    csi_effor_average.append(ResultsWorthEffort_Average)
    #print csi_collab_average
    #print csi_enjoy_average

# Create a column from the list
factordata['Collaboration_Average'] = csi_collab_average
factordata['Enjoyment_Average'] = csi_enjoy_average
factordata['Exploration_Average'] = csi_expl_average
factordata['Expressiveness_Average'] = csi_expr_average
factordata['Immersion_Average'] = csi_immer_average
factordata['ResultsWorthEffort_Average'] = csi_effor_average

# PART2

# Test the loaded data in Python
pairwisedata

# Create a list to store the data
csi_collab_count = 0
csi_enjoy_count = 0
csi_expl_count = 0
csi_expr_count = 0
csi_immer_count = 0
csi_effor_count = 0

csi_collab_count_total = []
csi_enjoy_count_total = []
csi_expl_count_total = []
csi_expr_count_total = []
csi_immer_count_total = []
csi_effor_count_total = []

i = 0

# For each row in the column,
for index, row in pairwisedata.iterrows() :
    for i in xrange(0, 15):
        eval = row[i]

        if eval == 'Work with other people':
            csi_collab_count = csi_collab_count + 1
        elif eval == 'Enjoy using the system or tool':
            csi_enjoy_count = csi_enjoy_count + 1
        elif eval == 'Explore many different ideas, outcomes, or possibilities':
            csi_expl_count = csi_expl_count + 1
        elif eval == 'Be creative and expressive':
            csi_expr_count = csi_expr_count + 1
        elif eval == 'Become immersed in the activity':
            csi_immer_count = csi_immer_count + 1
        elif eval == 'Produce results that are worth the effort I put in':
            csi_effor_count = csi_effor_count + 1

    # Print one of the vectors to check
    # print(csi_effor_count)

    # Store each average set of values per participant in a list
    csi_collab_count_total.append(csi_collab_count)
    csi_enjoy_count_total.append(csi_enjoy_count)
    csi_expl_count_total.append(csi_expl_count)
    csi_expr_count_total.append(csi_expr_count)
    csi_immer_count_total.append(csi_immer_count)
    csi_effor_count_total.append(csi_effor_count)

    # Set counters to zero
    csi_collab_count = 0
    csi_enjoy_count = 0
    csi_expl_count = 0
    csi_expr_count = 0
    csi_immer_count = 0
    csi_effor_count = 0

# print(csi_effor_count_total)

factordata['Collaboration_Count'] = csi_collab_count_total
factordata['Enjoyment_Count'] = csi_enjoy_count_total
factordata['Exploration_Count'] = csi_expl_count_total
factordata['Expressiveness_Count'] = csi_expr_count_total
factordata['Immersion_Count'] = csi_immer_count_total
factordata['ResultsWorthEffort_Count'] = csi_effor_count_total

CollaborationSub = factordata['Collaboration_Average'] * factordata['Collaboration_Count']
EnjoymentSub = factordata['Enjoyment_Average'] * factordata['Enjoyment_Count']
ExplorationSub = factordata['Exploration_Average'] * factordata['Exploration_Count']
ExpressivenessSub = factordata['Expressiveness_Average'] * factordata['Expressiveness_Count']
ImmersionSub = factordata['Immersion_Average'] * factordata['Immersion_Count']
ResultsWorthEffortSub = factordata['ResultsWorthEffort_Average'] * factordata['ResultsWorthEffort_Count']

CSIScore = sum([CollaborationSub, EnjoymentSub, ExplorationSub, ExpressivenessSub, ImmersionSub, ResultsWorthEffortSub])/1.5

# print(CSIScore)


collabmean = CollaborationSub.mean()
collabstd = CollaborationSub.std()
enjoymean = EnjoymentSub.mean()
enjoystd = EnjoymentSub.std()
explormean = ExplorationSub.mean()
explorstd = ExplorationSub.std()
expressmean = ExpressivenessSub.mean()
expressstd = ExpressivenessSub.std()
immersmean = ImmersionSub.mean()
immersstd = ImmersionSub.std()
effortmean = ResultsWorthEffortSub.mean()
effortstd = ResultsWorthEffortSub.std()

csv_columns = ['Term','Mean','SD']
dict_data = [
    {'Term': "Collaboration", 'Mean': collabmean, 'SD': collabstd},
    {'Term': "Enjoyment", 'Mean': enjoymean, 'SD': enjoystd},
    {'Term': "Exploration", 'Mean': explormean, 'SD': explorstd},
    {'Term': "Expressiveness", 'Mean': expressmean, 'SD': expressstd},
    {'Term': "Immersion", 'Mean': immersmean, 'SD': immersstd},
    {'Term': "ResultsWorthEffort", 'Mean': effortmean, 'SD': effortstd},
    ]

# Write results to a csv file
WriteDictToCSV(outputfactordata,csv_columns,dict_data)

# Load data from csv file into NumPy dataframe
factors = pd.read_csv(outputfactordata, sep=',', na_values='.')

CSIScoreByFactors = factors.sort_values("Mean", ascending = False)

# Write results to a csv file
CSIScore.to_csv(outputdata, header=["total"])
CSIScoreByFactors.to_csv(outputfactordata_sorted)
