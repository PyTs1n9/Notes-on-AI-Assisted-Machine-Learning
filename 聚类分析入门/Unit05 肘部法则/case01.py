import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

rng = np.random.default_rng(42)
X = np.r_[rng.normal(0, .3, (30, 2)), rng.normal(3, .3, (30, 2))]

ks, values = range(1, 7), []
for k in ks:
	model = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
	values.append(model.inertia_)

plt.plot(list(ks), values, marker="o")
plt.xlabel("簇数 K")
plt.ylabel("Inertia / SSE")
plt.title("肘部曲线")
plt.show()
