from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

rng = np.random.default_rng(42)
Path("reports").mkdir(exist_ok=True)
fields = ["Fresh", "Milk", "Grocery", "Frozen",
          "Detergents_Paper", "Delicassen"]
base = np.array([[24000, 2500, 3500, 6500, 800, 900],
                 [6000, 18000, 22000, 1800, 9500, 2200],
                 [7000, 4500, 3500, 12000, 1200, 7500],
                 [10000, 9000, 9500, 4500, 3200, 2800]], float)
g = rng.integers(0, 4, 200)
v = np.maximum(100, base[g] * rng.normal(1, .16, (200, 6))).round()
df = pd.DataFrame(v, columns=fields)
df.loc[2, "Milk"] = np.nan
df = pd.concat([df, df.iloc[[10]]], ignore_index=True)
df.loc[25, "Fresh"] = 999999
df = df.drop_duplicates()
df = df[df["Fresh"] < 100000].copy()
df[fields] = df[fields].fillna(df[fields].median())
Z = StandardScaler().fit_transform(df[fields])
rows = []
for k in range(2, 9):
	km = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = km.fit_predict(Z)
rows.append({"K": k, "Inertia": km.inertia_,
             "轮廓系数": silhouette_score(Z, labels),
             "DBI": davies_bouldin_score(Z, labels)})
table = pd.DataFrame(rows).round(4)
table.to_csv("reports/cluster_metrics.csv", index=False, encoding="utf-8-sig")
print(table)
print("文件存在：", Path("reports/cluster_metrics.csv").exists())
