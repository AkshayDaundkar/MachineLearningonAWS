import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDRegressor

# Load in the wine dataset
wine = datasets.load_wine()

# Create the wine `data` dataset as a dataframe and name the columns with `feature_names`
df = pd.DataFrame(wine["data"], columns=wine["feature_names"])

# Include the target as well
df['target'] = wine["target"]

# Split your data with these ratios: train: 0.8 | test: 0.2
df_train, df_test = train_test_split(df,test_size=0.2,random_state=0)


# How does the model perform on the training dataset and default model parameters?
# Using the hyperparameters in the requirements, is there improvement?
# Remember we use the test dataset to score the model
clf = LogisticRegression(random_state=0,max_iter=10000).fit(df_train.loc[:,df_train.columns !="target"],df_train["target"])
clf.score(df_test.loc[:,df_test.columns!="target"],df_test["target"])
