import pandas as pd
import xgboost as xgb

df = pd.DataFrame(
    [[1, 2, 0], [3, 4, 1], [5, 6, 0], [7, 8, 1]],
    columns=["num", "amount", "target"]
)
df_xgb = xgb.DMatrix(
    df[["num", "amount"]], label=df["target"]
)
params = {"eval_metric": "logloss", "objective": "binary:hinge"}
bst = xgb.train(params, df_xgb)

bst.predict(df_xgb)

# output
array([0., 1., 0., 1.], dtype=float32)
