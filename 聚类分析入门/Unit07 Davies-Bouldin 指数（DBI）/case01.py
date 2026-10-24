import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score

X = np.array([[0, 0], [.1, .2], [.2, .1], [5, 5], [5.1, 5.2], [5.2, 5.1]])
labels = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(X)
print("DBI：", davies_bouldin_score(X, labels))
