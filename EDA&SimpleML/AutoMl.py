#AutoGluon= framework that automates processing, creating and tuning of an ML model. creates baseline models. It is a part
#of a class model called AutoML, which automates the ml workflow.

import pandas as pd
from autogluon.tabular import TabularPredictor

df = pd.DataFrame(
    [[1, 2, 0], [3, 4, 1], [5, 6, 0], [7, 8, 1]],
    columns=["num", "amount", "target"]
)

predictor = TabularPredictor(label="target").fit(
    train_data=df,
    time_limit=60,
    presets="best_quality"
)

# output a summary of created models
predictor.fit_summary()

# evaluate best model from hyperparameter search
performance = predictor.evaluate(df)
