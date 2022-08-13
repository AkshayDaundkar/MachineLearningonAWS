import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.DataFrame(
    [[1, 2, 0], [3, 4, 1], [5, 6, 0], [7, 8, 1]],
    columns=["num", "amount", "target"]
)

clf = RandomForestClassifier().fit(df[["num", "amount"]], df["target"])

clf.score(df[["num", "amount"]], df["target"])
# 1.0

clf.predict([[1, 2]])
# array([0])


When tree-based models create nodes, they select the best features first to split data. In doing so, they inherently
 create feature importance rankings by creating the model itself. The higher the node in a tree-based model,
 the more important that feature is. This is useful not only to learn which models are most important, but also
  which features can be dropped from the dataset, since they provide little value to model performance. Smaller
   data also means faster training, and smaller overall dataset size.

dec trees can do classification clustering regression and feature selection
