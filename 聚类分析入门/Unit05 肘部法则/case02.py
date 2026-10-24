# 练习：将示例数据换成标准化后的六类消费；
# 尝试 K=1 到 8；
# 保存表格；
# 找可能的弯折位置。

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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
ks, values = list(range(1, 9)), []
for k in ks:
    model = KMeans(n_clusters=k, random_state=42, n_init=10).fit(Z)
    values.append(model.inertia_)
table = pd.DataFrame({"K": ks, "Inertia": values})
table.to_csv("reports/inertia.csv", index=False, encoding="utf-8-sig")
plt.plot(ks, values, marker="o")
plt.xlabel("簇数 K")
plt.ylabel("Inertia / SSE")
plt.title("客户聚类肘部曲线")
plt.xticks(ks)
plt.tight_layout()
plt.savefig("reports/elbow_curve.png", dpi=150)
plt.close()
print(table.round(2))
print("图存在：", Path("reports/elbow_curve.png").exists())