import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(os.path.join("outputs", "cleaned_customers.csv"), encoding="utf-8-sig")
feature_cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
X_raw = df[feature_cols]

# 方式1：sklearn标准化
scaler = StandardScaler()
X = scaler.fit_transform(X_raw)

# 方式2：手写公式
mu = X_raw.mean()
sd = X_raw.std(ddof=0)
X_manual = (X_raw - mu) / sd

print("最大差异:", np.abs(X_manual.to_numpy() - X).max())

# 结果
print(pd.DataFrame(X, columns=feature_cols)
      .agg(["mean", "std"]).round(6).to_string())

# 保存
with open("outputs/scaler_params.txt", "w", encoding="utf-8") as f:
	for c in feature_cols:
		f.write(f"{c}\tmean={mu[c]:.4f}\tstd={sd[c]:.4f}\n")
