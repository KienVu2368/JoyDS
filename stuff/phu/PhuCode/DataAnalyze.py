import numpy
import pandas
from pandas import set_option
import matplotlib.pyplot as plt

# Input file name, change to use a different file
outputFile = 'correlations.csv'
inputFile = 'Data-test.xlsx'

'''
Change the value in 'names' to match all the column name
'''
names = ['District', 'Gender', 'Class', 'Month', 'Session', 'Level', 'Mark', 'PUIA Metric', 'PUIB Metric']

dataset = pandas.read_excel(inputFile)

# Convert string data -> numeric
dataset = dataset.apply(lambda x: pandas.factorize(x)[0])

# Correlation raw data
set_option('display.width', 200)
set_option('precision', 3)
correlations = dataset.corr(method = 'pearson')
correlations.to_csv(outputFile, sep = ',', encoding = 'utf-8')

# Correlation graph
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin = -1, vmax = 1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()