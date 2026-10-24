from pathlib import Path
import numpy as np
import pandas as pd

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
df["Customer_ID"] = [f"C-{i}" for i in range(200)]
df.loc[2, "Milk"] = np.nan
df = pd.concat([df, df.iloc[[10]]], ignore_index=True)
df.loc[25, "Fresh"] = 999999
df = df.drop_duplicates()
df = df[df["Fresh"] < 100000].copy()  # 该值是脚本故意制造的异常
df[fields] = df[fields].fillna(df[fields].median())
X = df[fields]
X.to_csv("data/clean_customers.csv", index=False, encoding="utf-8-sig")
Path("reports/cleaning_note.txt").write_text(
	f"清理后客户数：{len(X)}\n消费字段：{fields}\n编号未参与聚类。\n",
	encoding="utf-8")
print(X.head())
print("清理文件存在：", Path("data/clean_customers.csv").exists())
