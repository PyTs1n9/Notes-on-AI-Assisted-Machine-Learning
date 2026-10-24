from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)
fields = ["Fresh", "Milk", "Grocery", "Frozen",
          "Detergents_Paper", "Delicassen"]
base = np.array([[24000, 2500, 3500, 6500, 800, 900],
                 [6000, 18000, 22000, 1800, 9500, 2200],
                 [7000, 4500, 3500, 12000, 1200, 7500],
                 [10000, 9000, 9500, 4500, 3200, 2800]], float)
g = rng.integers(0, 4, 200)
v = np.maximum(100, base[g] * rng.normal(1, .16, (200, 6))).round()
df = pd.DataFrame(v, columns=fields)
df["Customer_ID"] = [f"C-{i}" for i in range(200)]
df.loc[3, "Milk"] = np.nan
df = pd.concat([df, df.iloc[[8]]], ignore_index=True)
df.loc[20, "Fresh"] = 999999
df = df.drop_duplicates()
df = df[df["Fresh"] < 100000].copy()
df[fields] = df[fields].fillna(df[fields].median())


scaler = StandardScaler()
Z = scaler.fit_transform(df[fields])
scaled = pd.DataFrame(Z, columns=fields)
scaled.to_csv("data/scaled_customers.csv", index=False, encoding="utf-8-sig")


print("均值：", scaled.mean().round(2).to_dict())
print("标准差：", scaled.std(ddof=0).round(2).to_dict())
print("文件存在：", Path("data/scaled_customers.csv").exists())
