import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([
	[0, 0],
	[.1, .2],
	[.2, .1],
	[5, 5],
	[5.1, 5.2],
	[5.2, 5.1]
])
scores = []
for k in range(2, 5):
    labels = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    ).fit_predict(X)

    scores.append(silhouette_score(X, labels))
print("轮廓系数：", scores)
