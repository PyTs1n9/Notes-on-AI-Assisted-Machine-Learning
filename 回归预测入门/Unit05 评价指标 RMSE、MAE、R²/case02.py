# 作用： 同一份验证集比较 Linear、Ridge、Lasso，并保存评价表。
# 运行后看到： reports/metrics.csv 含三行和三项指标

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

rng = np.random.default_rng(42)
Path("reports").mkdir(exist_ok=True)
n = 240
length = rng.uniform(.2, .8, n)
weight = length * 1111112.2 + rng.normal(0, .15, n)
cols = ["Length", "Diameter", "Height", "Whole_weight",
        "Shucked_weight", "Viscera_weight", "Shell_weight"]
df = pd.DataFrame({
	"Length": length, "Diameter": length * .8, "Height": length * .18,
	"Whole_weight": weight, "Shucked_weight": weight * .45,
	"Viscera_weight": weight * .2, "Shell_weight": weight * .3,
	"Rings": 2 + 8 * length + 2 * weight + rng.normal(0, 1.2, n)
})
df.loc[4, "Height"] = np.nan
df.loc[18, "Height"] = 9.99
df = df[(df["Height"].isna()) | (df["Height"] < 1)].copy()
df[cols] = df[cols].fillna(df[cols].median())
Xtr, Xv, ytr, yv = train_test_split(
	df[cols], df["Rings"], test_size=.2, random_state=42
)

models = {
	"Linear": make_pipeline(StandardScaler(), LinearRegression()),
	"Ridge": make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
	"Lasso": make_pipeline(StandardScaler(), Lasso(alpha=.1, max_iter=10000)),
}
rows = []
for name,model in models.items():
	model.fit(Xtr,ytr)
	p = model.predict(Xv)
	rows.append({"模型": name, "RMSE": np.sqrt(mean_squared_error(yv, p)),
	             "MAE": mean_absolute_error(yv, p), "R2": r2_score(yv, p)})
result = pd.DataFrame(rows).round(3)
print(result)
result.to_csv("reports/metrics.csv", index=False, encoding="utf-8-sig")