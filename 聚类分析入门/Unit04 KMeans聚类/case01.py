import numpy as np
from sklearn.cluster import KMeans

X = np.array([
	[1, 1],
	[1.2, 1.1],
	[8, 8],
	[8.2, 8.1]
])
model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(X)
print("标签：", model.labels_)
print("聚类中心：", model.cluster_centers_)
