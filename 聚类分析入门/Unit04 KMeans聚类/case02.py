# 练习中对消费数据先标准化再聚类，
# 将标签加回客户表，
# 并还原中心。

# 四簇客户分群，保存客户和标签，以及以原消费金额表示的中心表。

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)
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
df["Customer_ID"] = [f"C-{i:04d}" for i in range(200)]
df.loc[5, "Milk"] = np.nan
df = pd.concat([df, df.iloc[[12]]], ignore_index=True)
df.loc[30, "Fresh"] = 999999
df = df.drop_duplicates()
df = df[df["Fresh"] < 100000].copy()
df[fields] = df[fields].fillna(df[fields].median())


scaler = StandardScaler()
Z = scaler.fit_transform(df[fields])


model = KMeans(n_clusters=4, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(Z)
amounts = scaler.inverse_transform(model.cluster_centers_)


centers = pd.DataFrame(amounts, columns=fields)
centers.insert(0, "Cluster", range(4))
df.to_csv("data/customer_clusters.csv", index=False, encoding="utf-8-sig")
centers.to_csv("reports/cluster_centers.csv", index=False, encoding="utf-8-sig")
print(df[["Customer_ID", "Cluster"]].head())
print(centers.round(0))
