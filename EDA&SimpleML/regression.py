from sklearn.linear_model import LinearRegression

features = [[5, 3.4, 6], [1, 0.4, 10], [2, 0.1, 1]]
target = [1.4, 0.5, 1]

reg = LinearRegression().fit(features, target)

# Score model with features and target
print(reg.score(features, target))
# Predict new values based on features
print(reg.predict(features))


# output
1.0
[1.4 0.5 1. ]
