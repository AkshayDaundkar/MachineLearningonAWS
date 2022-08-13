from sklearn.cluster import KMeans

features = [[5, 3.4, 6], [1, 0.4, 10], [2, 0.1, 1]]
# Cluster into 3 groups
kmeans = KMeans(n_clusters=3).fit(features)

# Prints which data point belongs to which cluster group
print(kmeans.labels_)
# Prints the metric of how clustering performed
print(kmeans.inertia_)

# output
[0 2 1]
0.0



#another KMeans


from sklearn.cluster import KMeans

# We already know the number of clusters, we can use during fit
kmeans = KMeans(n_clusters=3, random_state=0).fit(df[iris["feature_names"]])

# Print the labels to see what value is in what cluster
kmeans.labels_

#output
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2,
       2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2,
       2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0], dtype=int32)
