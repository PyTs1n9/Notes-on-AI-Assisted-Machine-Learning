import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATASET = "dataset"
df = pd.read_csv(os.path.join(DATASET, "Wholesale_customers_data.csv"))
print(f"字段信息：\n{df.describe()}")

cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
summary = df[cols].agg(["min", "max", "mean", "std"]).T
print(f"查看 6 个字段的信息：\n{summary}")


# 思考不同量纲是否会影响距离: 会影响，聚类是欧氏距离，量纲大小会影响距离，会导致主导的距离不同

scaler = StandardScaler()
standardscaler_df = scaler.fit_transform(df[cols])
print(f"标准化后前10行：\n{standardscaler_df[:10]}")

K = 3
model = KMeans(n_clusters=K, random_state=42, n_init=100)
labels = model.fit_predict(standardscaler_df)
center = model.cluster_centers_

counts = pd.Series(labels).value_counts().sort_values()
print("统计每个 cluster 的客户:")
for k,c in counts.items():
	print(f"簇{k}：{c}")

print(f"cluster_centers_: {center.shape}")

origin_centers = scaler.inverse_transform(center)
print(origin_centers)

print("未标准化聚类结果：")
ctr = pd.DataFrame(origin_centers, columns=cols).round(3)
ctr.index.name = "簇"
print(ctr.to_string())

print("标准化聚类结果：")
k_ctr = pd.DataFrame(center, columns=cols).round(3)
k_ctr.index.name = "簇"
print(k_ctr.to_string())

plt.figure(figsize=(8, 6))
plt.scatter(
    df["Fresh"],
    df["Milk"],
    c=labels,          # 用聚类标签着色
    alpha=0.7
)
plt.xlabel("Fresh")
plt.ylabel("Milk")
plt.title("Fresh—Milk Scatter")
plt.colorbar(label="Cluster")
plt.show()