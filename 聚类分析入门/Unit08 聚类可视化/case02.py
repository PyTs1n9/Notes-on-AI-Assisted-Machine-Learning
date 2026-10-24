from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

rng = np.random.default_rng(42)
out = Path("reports")
out.mkdir(exist_ok=True)
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
df.loc[22, "Fresh"] = 999999
df = df.drop_duplicates()
df = df[df["Fresh"] < 100000].copy()
df[fields] = df[fields].fillna(df[fields].median())
scaler = StandardScaler()
Z = scaler.fit_transform(df[fields])
model = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = model.fit_predict(Z)
# 二维图只展示鲜品和奶类 {#二维图只展示鲜品和奶类 }
plt.figure()
plt.scatter(df["Fresh"], df["Milk"], c=labels, cmap="tab10", alpha=.7)
plt.xlabel("鲜品消费")
plt.ylabel("奶类消费")
plt.title("二维客户分群")
plt.tight_layout()
plt.savefig(out / "customer_2d.png", dpi=150)
plt.close()
# 三维图增加杂货字段 {#三维图增加杂货字段 }
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(df["Fresh"], df["Milk"], df["Grocery"], c=labels, cmap="tab10")
ax.set_xlabel("鲜品")
ax.set_ylabel("奶类")
ax.set_zlabel("杂货")
plt.tight_layout()
plt.savefig(out / "customer_3d.png", dpi=150)
plt.close()
# 还原中心金额后制作热力图 {#还原中心金额后制作热力图 }
amounts = scaler.inverse_transform(model.cluster_centers_)
center = pd.DataFrame(amounts, columns=fields)
plt.figure(figsize=(9, 4))
plt.imshow(center, aspect="auto", cmap="YlOrRd")
plt.colorbar(label="消费金额")
plt.xticks(range(6), fields, rotation=30, ha="right")
plt.yticks(range(4), ["簇0", "簇1", "簇2", "簇3"])
plt.title("聚类中心热力图")
plt.tight_layout()
plt.savefig(out / "center_heatmap.png", dpi=150)
plt.close()
for p in out.glob("*.png"):
	print(p.name, "存在：", p.exists(), "大小：", p.stat().st_size)
