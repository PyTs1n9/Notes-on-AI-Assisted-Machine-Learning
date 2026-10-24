import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

Path("dataset").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)

df = pd.read_csv("dataset/Wholesale_customers_data.csv", encoding="utf-8-sig")
cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
k_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

scaler = StandardScaler()
standard_data = scaler.fit_transform(df[cols])
k_inertia_list = []

for k in k_list:
	model = KMeans(n_clusters=k, random_state=42, n_init=10)
	model.fit(standard_data)
	k_inertia_list.append(model.inertia_)

inertia_df = pd.DataFrame({
	"K": k_list,
	"values": k_inertia_list
}).to_csv("output/k_inertia.csv", index=False, encoding="utf-8-sig")

plt.plot(k_list, k_inertia_list, marker="o")
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("K-inertia")
plt.show()

choose_Ks, choose_value = [5, 6], []
for k in choose_Ks:
	model = KMeans(n_clusters=k, random_state=42, n_init=10)
	model.fit(standard_data)
	centers = pd.DataFrame(
		scaler.inverse_transform(model.cluster_centers_),
		columns=cols
	)
	centers.insert(0, "簇编号", range(k))
	counts = pd.Series(model.labels_).value_counts().rename(f"K={k}")
	choose_value.append(counts)
	print(f"k: {k}, counts: {counts}")
	print(centers.round(2).to_string(index=False))

comparison = pd.concat(choose_value,axis=1).fillna(0).astype(int)
comparison.index.name = "簇编号"
print(comparison)