# 使用完整rings特征；fit训练集；
# 打印特征名和系数；
# 计算验证误差；更改 alpha 并记录非零系数数量。
# 若使用 Pipeline，模型本体通过 named_steps 读取。

# 作用： 训练 Lasso、输出指标和系数表。
# 运行后看到： reports/lasso_coefficients.csv 生成，含每个测量字段系数。
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error,root_mean_squared_error,r2_score,mean_absolute_error
rng = np.random.default_rng(42)
Path("reports").mkdir(exist_ok=True)
n = 260
length = rng.uniform(.2, .8, n)
whole = 2.2 * length + rng.normal(0, .15, n)
cols = ["Length", "Diameter", "Height", "Whole_weight",
        "Shucked_weight", "Viscera_weight", "Shell_weight"]
df = pd.DataFrame({
	"Length": length, "Diameter": length * .8, "Height": length * .18,
	"Whole_weight": whole, "Shucked_weight": whole * .45,
	"Viscera_weight": whole * .2, "Shell_weight": whole * .3,
	"Rings": 2 + 8 * length + 2 * whole + rng.normal(0, 1.2, n)
})
df.loc[5, "Height"] = np.nan
df.loc[20, "Height"] = 9.99
df = df[(df["Height"].isna()) | (df["Height"] < 1)].copy()
df[cols] = df[cols].fillna(df[cols].median())
Xtr, Xv, ytr, yv = train_test_split(
	df[cols], df["Rings"], test_size=.2, random_state=42
)
model = make_pipeline(StandardScaler(), Lasso(alpha=0.1, max_iter=10000))
model.fit(Xtr,ytr)
pred = model.predict(Xv)
print("RMSE", np.sqrt(mean_squared_error(yv, pred)))
print("MAE", mean_absolute_error(yv, pred), "R2", r2_score(yv, pred))

coef = pd.DataFrame({
	"特征": cols, "系数": model.named_steps["lasso"].coef_
})
print(coef)
coef.to_csv("reports/lasso_coefficients.csv", index=False, encoding="utf-8-sig")
