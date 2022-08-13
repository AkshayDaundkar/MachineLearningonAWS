import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

# R2(R squared) (coefficient of determination) regression score function.
#Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y,
#disregarding the input features, would get a  score of 0.0.
#R2 - measures the proportion of variance.


# Load in the diabetes dataset
diabetes = datasets.load_diabetes()
diabetes

# Create the diabetes `data` dataset as a dataframe and name the columns with `feature_names`
df = pd.DataFrame(diabetes["data"], columns=diabetes["feature_names"])

# Include the target as well
df["target"] = diabetes["target"]

# train: 0.8 | test: 0.2
df_train, df_test = train_test_split(df, test_size=0.2, random_state=0)

# train: 0.6 | validation: 0.2
df_train, df_val = train_test_split(df_train, test_size=0.25, random_state=0)

# Final dataset sizes: train: 0.6, validation: 0.2, text: 0.2

# How does the model perform on the entire dataset and default model parameters
reg = Ridge().fit(df[diabetes["feature_names"]], df["target"])
all_df_score = reg.score(df[diabetes["feature_names"]], df["target"])
all_df_score

# How does the model perform on the training dataset and default model parameters
# Remember we use the validation dataset score the model
reg = Ridge().fit(df_train[diabetes["feature_names"]], df_train["target"])
val_df_score = reg.score(df_val[diabetes["feature_names"]], df_val["target"])
val_df_score



#Bar plot of all scores

pd.Serties(
{
"all_df_score":all_df_score,
"val_df_score":val_df_score
}
).plot(kind="bar",legend=False,title="R2 Score of Ridge Model")
