#in sagemaker studio you choose an image, like data science or base python image to spin up your sagemaker notebook
#image runs on ec2 instance


#EDA: use pandas dataframes,

import pandas as import pd

df = pd.DataFrame(
  {
    'a': [1, 2, 3, 4, 5],
    'b': ['a', 'b', 'c', 'd', 'f'],
    'c': [5, 4, 3, 2, 1],
  }
)

print(df.describe())

              a         c
count  5.000000  5.000000
mean   3.000000  3.000000
std    1.581139  1.581139
min    1.000000  1.000000
25%    2.000000  2.000000
50%    3.000000  3.000000
75%    4.000000  4.000000
max    5.000000  5.000000

# df.hist() plots histograms
# Plot the the distribution of values
# Helps identify outliers or unexpected values
# Normal, Uniform, chi-square, F are examples of different distributions


# df.corr() calculates a correlation matrix
# Correlation is the relationship between two variables
# Values from correlation range from -1.0 to 1.0
# -1.0 is a strong negative relationship
# 1.0 is a strong positive relationship
# Diagonal matrix values always 1.0
# Strong positive or negative relationships add little to ML models
print(df.corr())
"""
     a    c
a  1.0 -1.0
c -1.0  1.0
"""


#Which of these pandas DataFrames are equal to the table below?

a	b
0	1	a
1	2	b
2	3	c
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})


df = pd.DataFrame([[1, 'a'], [2, 'b'], [3, 'c']], columns=['a', 'b'])

df = pd.DataFrame(np.array([[1, 'a'], [2, 'b'], [3, 'c']])) df.columns = ['a', 'b']

#eda is a cloud based solution for eda and data transoformations on AWS
#helps with the creation of ETL pipelines

#data wrangler uses s3, uses s3 import data
