
import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# Load in the iris dataset
iris = datasets.load_iris()
iris.keys()

Create the iris `data` dataset as a dataframe and name the columns with `feature_names`
df = pd.DataFrame(iris["data"], columns=iris["feature_names"])

# Include the target as well
df['target'] = iris["target"]

# Check your dataframe by `.head()`
df.head()
print(df["target"])

# Fit a standard regression model, we've done this in other exercises
#you do df[iris["feature_names"]] with double brackets bc unlike target feature_names spans across several columns
reg = LinearRegression().fit(df[iris["feature_names"]], df["target"])

# Score the model on the same dataset
reg.score(df[iris["feature_names"]],df["target"])

# Predicting values shows they are not that useful to a classification model
reg.predict(df[iris["feature_names"]])
