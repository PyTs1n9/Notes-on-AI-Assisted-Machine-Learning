import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(os.path.join("outputs", "cleaned_customers.csv"), encoding="utf-8-sig")
feature_cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
X_raw = df[feature_cols]

# 方式1：sklearn标准化
scaler = StandardScaler()
X = scaler.fit_transform(X_raw)

K_FINAL = 4
km = KMeans(n_clusters=K_FINAL, init="k-means++", n_init=20, random_state=42, max_iter=300)
labels = km.fit_predict(X)  # (441,) 每个客户所属簇
centers = km.cluster_centers_  # (4,6) 簇中心坐标
inertia = km.inertia_  # SSE

print(f"labels 形状 {labels.shape}，取值{sorted(set(labels.tolist()))}")
print(f"cluster_centers_ 形状 {centers.shape}")
print(f"inertia_ （SSE） = {inertia:.4f}")
print(f"n_iter_ = {km.n_iter_}")

# 簇规模
vc = pd.Series(labels).value_counts().sort_index()
for k,c in vc.items():
	print(f"簇 {k}:{c:>4d} 人 ({c / len(df) * 100:.1f}%)")

# 簇中心
ctr = pd.DataFrame(centers,columns=feature_cols).round(3)
ctr.index.name = "簇"
print(ctr.to_string())