import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[1000, 1], [2000, 2], [3000, 3]], dtype=float)
scaler = StandardScaler()
Z = scaler.fit_transform(X)
print(Z.round(2))
print("列均值：", Z.mean(axis=0).round(2))
