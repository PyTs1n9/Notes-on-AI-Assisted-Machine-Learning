import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

Path("dataset").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
output_dir = Path("output")
dataset_dir = Path("dataset")
csv_dir = dataset_dir / "Wholesale_customers_data.csv"
cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
df = pd.read_csv(csv_dir, encoding="utf-8-sig")

scaler = StandardScaler()
standard_data = scaler.fit_transform(df[cols])
k_inertia_list = []
k_silhouette_score_list = []
k_dbi_list = []

for k in range(2, 11):
	model = KMeans(n_clusters=k, random_state=42, n_init=10)
	labels = model.fit_predict(standard_data)
	k_inertia_list.append(model.inertia_)
	k_silhouette_score_list.append(silhouette_score(standard_data, labels))
	k_dbi_list.append(davies_bouldin_score(standard_data, labels))

new_df = pd.DataFrame({
	"K": range(2, 11),
	"Inertia": k_inertia_list,
	"Silhouette": k_silhouette_score_list,
	"DBI": k_dbi_list
})
k_metrics_df = output_dir / "k_metrics.csv"
new_df.to_csv(k_metrics_df, index=False, encoding="utf-8-sig")

lists = [k_inertia_list, k_silhouette_score_list, k_dbi_list]
lists_index = ["Inertia", "Silhouette", "DBI"]
index = 0
for i in lists:
	plt.plot(range(2, 11), i, marker="o")
	plt.xlabel("K")
	plt.ylabel(lists_index[index])
	plt.title(f"K-{lists_index[index]}-Table")
	index += 1
	plt.show()

k_values = np.array(range(2, 11))
best_silhouette_k = k_values[np.argmax(k_silhouette_score_list)]
best_dbi_k = k_values[np.argmin(k_dbi_list)]

print("轮廓系数推荐 K:", best_silhouette_k)
print("DBI 推荐 K:", best_dbi_k)

inertia = np.array(k_inertia_list)

second_difference = np.diff(inertia, n=2)
elbow_index = np.argmax(second_difference)
elbow_k = k_values[1:][elbow_index]

print("Elbow 推荐 K:", elbow_k)
