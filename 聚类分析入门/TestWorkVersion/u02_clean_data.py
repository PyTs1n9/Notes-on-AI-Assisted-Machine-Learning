import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

OUT = "outputs"

# 加载
df = pd.read_csv(os.path.join(OUT, "wholesale_customers.csv"), encoding="utf-8-sig")
feature_cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
meta_cols = ["Channel", "Region"]
print(f"原始数据：{df.shape}")

# 去重
n_before = len(df)
df = df.drop_duplicates(subset=meta_cols + feature_cols, keep="first").reset_index(drop=True)
print(f"去重：{n_before} -> {len(df)}")

# 缺失值
print(df[feature_cols].isna().sum().to_string())

imputer = SimpleImputer(strategy="median")
df[feature_cols] = imputer.fit_transform(df[feature_cols])
print(f"填充后总缺失数：{df[feature_cols].isna().sum().sum()}")

# 异常值
for c in feature_cols:
	q1, q3 = df[c].quantile(0.25), df[c].quantile(0.75)
	iqr = q3 - q1
	lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
	n_out = ((df[c] < lo) | (df[c] > hi)).sum()
	df[c] = df[c].clip(lower=max(0.0, lo), upper=hi)  # 关键 不drop
	print(f"{c:<20} 离群={n_out:>3d}")

df.to_csv(os.path.join(OUT, "cleaned_customers.csv"),
          index=False, encoding="utf-8-sig")


