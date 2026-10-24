from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)

fields = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]

profiles = np.array([
	[24000, 2500, 3500, 6500, 800, 900],
	[6000, 18000, 22000, 1800, 9500, 2200],
	[7000, 4500, 3500, 12000, 1200, 7500],
	[10000, 9000, 9500, 4500, 3200, 2800]
], dtype=float)

group = rng.integers(0, 4, 200)
values = profiles[group] * rng.normal(1.0, 0.16, (200, 6))
values = np.maximum(values, 100).round()
df = pd.DataFrame(values, columns=fields)
df["Channel"] = rng.choice([1, 2], 200)
df["Region"] = rng.choice([1, 2, 3], 200)
df["Customer_ID"] = [f"C-{i:04d}" for i in range(200)]

df.loc[3, "Milk"] = np.nan
df.loc[15, "Grocery"] = np.nan
df = pd.concat([df, df.iloc[[20, 21]]], ignore_index=True)
df.loc[30, "Fresh"] = 999999
df.to_csv("data/wholesale_customers.csv", index=False, encoding="utf-8-sig")
print("数据形状：", df.shape)
print("缺失值：\n", df.isna().sum())
print("重复行：", df.duplicated().sum())
print("文件存在：", Path("data/wholesale_customers.csv").exists())
