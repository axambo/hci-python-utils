# HCI Python Utils

Copyright (c) 2018 [Anna Xambó](a.xambo@qmul.ac.uk)

## Introduction

This code implements established HCI metrics in Python, such as the **system usability scale** (SUS) [Brooke, 1996] and the **creativity-support index** (CSI) [Carroll et al., 2009]. The SUS is a survey metric for usability assessment of systems, tools and interfaces. The CSI is another survey metric that helps to assess the level of creativity support provided by systems, tools and interfaces.

## Setup

* Before launching the code, make sure to install the [pandas library](https://pandas.pydata.org/).
* Other essential Python libraries that you will need, mostly for plotting the results, are: NumPy and matplotlib.

## SUS

### Expected Collected Data

The questionnaire is expected to have the following 10 questions:

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.  

The answers are formatted using a rating scale (Likert scale) of five levels (Strongly disagree, Disagree, Neutral, Agree, Strongly agree) that range from 1 to 5.

### SUS Calculation

To calculate the SUS score, first sum the score contributions from each item. Each item's score contribution will range from 0 to 4. For items 1,3,5,7 and 9, the score contribution is the scale position minus 1. For items 2,4,6,8 and 10, the contribution is 5 minus the scale position. Multiply the sum of the scores by 2.5 to obtain the overall value of SUS. SUS scores have a range of 0 to 100, where the higher the value, the higher level of usability.

### Application Start

You should start having csv file with the results, see `SUS-input-data.csv` for an example.

1. Go to the Terminal and launch the python script `sus.py`:

	```
	python sus.py SUS-input-data.csv SUS-results.csv
	```

	where you should replace the first argument `SUS-input-data.csv` with the csv filename of the collected data, which should be organized by participants and questions, and the second argument `SUS-results.csv` with the filename that will store the resulting SUS index for each participant.

2. Once you get the results, feel free to use either the `SUS-plot.py` script for a single boxplot or the `SUS-plot-compare.py` script for multiple boxplots that represent various systems.

	For a single boxplot:
	
	```
	python sus-plot.py SUS-results.csv
	```
	
	where you should replace the first argument `SUS-results.csv` with the csv filename of the results of the SUS metric.
	
	For multiple boxplots:
	
	```
	python sus-plot-compare.py SUS-results1.csv SUS-results2.csv SUS-results3.csv
	```
	where you should replace the three arguments `SUS-results1.csv`, `SUS-results2.csv` and `SUS-results3.csv` with the csv filenames of the results of the SUS metric by each tool you would like to compare.

## CSI

### Expected Collected data

There are 6 orthogonal factors (*exploration*, *expressiveness*, *enjoyment*, *immersion*, *collaboration*, *results*, *worth effort*) and in the survey there are 2 questions for each (with a total of 12 questions). If you were evaluating more than one system, this set of questions would be repeated for each system:

1. I was satisfied with what I got out of the system or tool. (*ResultsWorthEffort*)
2. It was easy for me to explore many different ideas, options, designs, or outcomes, using this system or tool. (*Exploration*)
3. The system or tool allowed other people to work with me easily (mark 0 if this question is not relevant for the task). (*Collaboration*)
4. I would be happy to use this system or tool on a regular basis. (*Enjoyment*)
5. I was able to be very expressive and creative while doing the activity inside this system or tool. (*Expressiveness*)
6. My attention was fully tuned to the activity, and I forgot about the system or tool that I was using. (*Immersion*)
7. I enjoyed using this system or tool. (*Enjoyment*)
8. The system or tool was helpful in allowing me to track different ideas, outcomes, or possibilities. (*Exploration*)
9. What I was able to produce was worth the effort I had to exert to produce it. (*ResultsWorthEffort*)
10. The system or tool allowed me to be very expressive. (*Expressiveness*)
11. It was really easy to share ideas and designs with other people inside this system or tool (mark 0 if this question is not relevant for the task). (*Collaboration*)
12. I became so absorbed in the activity that I forgot about the system or tool that I was using. (*Immersion*)

In the survey, there are also 15 pairwise factor questions, which is used to rank the 6 factors. If you were evaluating more than one system, this set of questions would only be asked once, but the results would be repeated in the computation for each system evaluated:

1. When doing this task, it's most important that I'm able to...
	- Explore many different ideas, outcomes, or possibilities. (*Exploration*)
	- Work with other people. (*Collaboration*)
2. When doing this task, it's most important that I'm able to...
	- Be creative and expressive. (*Expressivity*)
	- Produce results that are worth the effort I put in. (*Resultswortheffort*)
3. When doing this task, it's most important that I'm able to...
	- Enjoy using the system or tool. (*Enjoyment*)
	- Become immersed in the activity. (*Immersion*)
4. When doing this task, it's most important that I'm able to...
	- Become immersed in the activity. (*Immersion*)
	- Produce results that are worth the effort I put in. (*Resultswortheffort*)
5. When doing this task, it's most important that I'm able to... 
	- Work with other people. (*Collaboration*).
	- Enjoy using the system or tool. (*Enjoyment*)
6. When doing this task, it's most important that I'm able to...
	- Produce results that are worth the effort I put in. (*Resultswortheffort*)
	- Explore many different ideas, outcomes, or possibilities. (*Exploration*)
7. When doing this task, it's most important that I'm able to...
	- Be creative and expressive. (*Expressivity*)
	- Become immersed in the activity. (*Immersion*)
8. When doing this task, it's most important that I'm able to...
	- Work with other people. (*Collaboration*)
	- Produce results that are worth the effort I put in. (*Resultswortheffort*)
9. When doing this task, it's most important that I'm able to...
	- Be creative and expressive. (*expressivity*)
	- Enjoy using the system or tool. (*enjoyment*)
10. When doing this task, it's most important that I'm able to...
	- Explore many different ideas, outcomes, or possibilities. (*Exploration*)
	- Become immersed in the activity. (*Immersion*)
11. When doing this task, it's most important that I'm able to...
	- Work with other people. (*Collaboration*)
	- Be creative and expressive. (*Expressivity*)
12. When doing this task, it's most important that I'm able to...
	- Produce results that are worth the effort I put in. (*Resultswortheffort*)
	- Enjoy using the system or tool. (*Enjoyment*)
13. When doing this task, it's most important that I'm able to...
	- Explore many different ideas, outcomes, or possibilities. (*Exploration*)
	- Be creative and expressive. (*Expressivity*)
14. When doing this task, it's most important that I'm able to...
	- Work with other people. (*Collaboration*)
	- Become immersed in the activity. (*Immersion*)
15. When doing this task, it's most important that I'm able to...
	- Explore many different ideas, outcomes, or possibilities. (*Exploration*)
	- Enjoy using the system or tool. (*Enjoyment*)

The answers are formatted using a rating scale (Likert scale) that range from 0 to 10 (from Highly Disagree to Highly Agree).

For each participant/system, you should end up with a CSI index (0-100) that indicates the level of creativity support afforded by the system.

### CSI Calculation

In the paper's version, an average is calculated first between the two sets of questions of the first block, ending with 6 average values one for each factor. Then, each average factor is multiplied by  the weighted result for each factor based in the pairwise comparisons. The overall summation is divided into 1.5. The implementation is informed by both the paper and the [CSI Jar implementation](http://www.erincherry.net/#csi) by Erin Cherry.

### Application Start

You should start having two csv files with the results, see `CSI-input-factor-data.csv` (12 factor questions) and `CSI-input-pairwise-data.csv` (15 pairwise questions) for an example. Both are needed to calculate the CSI value.

1. Go to the Terminal and launch the python script `csi.py`:

	```
	python csi.py
	```
	
	where you can either stick with the names of the input/output csv files provided by the python script `csi.py`, or pass them as arguments as it is shown in the SUS example. The current file names are:
	
	* *factordata*: `csi-input-factor-data.csv`
	* *pairwisedata*: `csi-input-pairwise-data.csv`
	* *outputdata*: `csi-results.csv`
	* *outputfactordata*: `csi-factors-results.csv`
	* *outputfactordata_sorted*: `csi-factors-results-sorted.csv`

## References

* Brooke, John. [SUS - A Quick and Dirty Usability Scale](https://hell.meiert.org/core/pdf/sus.pdf). Usability Evaluation in Industry, 189(194):4-7, 1996.
* Carroll, Erin A.; Latulipe, Celine; Fung, Richard and Terry, Michael. [Creativity Factor Evaluation: Towards a Standardized Survey Metric for Creativity Support](https://s3.amazonaws.com/academia.edu.documents/30803747/CSI_-_Creativity_Factor_Evaluation_Towards_a_Standardized.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1518631554&Signature=wx3RKIqVzwVNBvl7dzfDpupovqE%3D&response-content-disposition=inline%3B%20filename%3DCreativity_factor_evaluation_Towards_a_s.pdf). In Proceedings of ACM Creativity and Cognition (CC '09), pages 127-136, Berkeley, CA, USA, 2009.

## License

[The ISC License](http://opensource.org/licenses/ISC).
