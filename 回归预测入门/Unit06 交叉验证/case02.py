# 作用： 在 rings 训练集做五折评估并搜索 Ridge alpha。
# 运行后看到： 输出每折 RMSE、最佳参数和最终验证 RMSE；
# reports/cv_scores.csv 存在。

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(42)
Path("reports").mkdir(exist_ok=True)
n = 280
length = rng.uniform(.2, .8, n)
w = 2.2*length + rng.normal(0, .15, n)
cols = ["Length", "Diameter", "Height", "Whole_weight",
"Shucked_weight", "Viscera_weight", "Shell_weight"]
df = pd.DataFrame({
"Length": length, "Diameter": length*.8, "Height": length*.18,
"Whole_weight": w, "Shucked_weight": w*.45, "Viscera_weight": w*.2,
"Shell_weight": w*.3, "Rings": 2+8*length+2*w+rng.normal(0, 1.2, n)
})
df.loc[2, "Height"] = np.nan
df.loc[12, "Height"] = 9.99
df = df[(df["Height"].isna()) | (df["Height"] < 1)].copy()
df[cols] = df[cols].fillna(df[cols].median())
Xtr, Xv, ytr, yv = train_test_split(
df[cols], df["Rings"], test_size=.2, random_state=42
)

base = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
scores = cross_val_score(base, Xtr, ytr, cv=5,
	scoring="neg_mean_squared_error")
fold_rmse = np.sqrt(-scores)

search = GridSearchCV(
make_pipeline(StandardScaler(), Ridge()),
{"ridge__alpha": [.01, .1, 1, 10, 100]},
cv=5, scoring="neg_mean_squared_error"
)

search.fit(Xtr, ytr)
p = search.best_estimator_.predict(Xv)
print("每折 RMSE：", fold_rmse.round(3))
print("最佳参数：", search.best_params_)
print("验证 RMSE：", np.sqrt(mean_squared_error(yv, p)))
pd.DataFrame({"折": range(1, 6), "RMSE": fold_rmse}).to_csv(
"reports/cv_scores.csv", index=False, encoding="utf-8-sig")