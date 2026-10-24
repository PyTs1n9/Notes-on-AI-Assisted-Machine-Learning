# 作用： 自动生成无外部依赖数据，训练线性模型、算指标并保存对照图。
# 运行后看到： 终端输出三项指标，reports/linear_prediction.png 存在。

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

rng = np.random.default_rng(42)
Path("reports").mkdir(exist_ok=True)
n = 300
length = rng.uniform(.2, .8, n)
whole = length * 2.2 + rng.normal(0, .15, n)
cols = ["Length", "Diameter", "Height", "Whole_weight",
		"Shucked_weight", "Viscera_weight", "Shell_weight"]
df = pd.DataFrame({
	"Length": length, "Diameter": length*.8, "Height": length*.18,
	"Whole_weight": whole, "Shucked_weight": whole*.45,
	"Viscera_weight": whole*.2, "Shell_weight": whole*.3,
	"Rings": 2 + 8*length + 2*whole + rng.normal(0, 1.2, n)
})
df["Rings"] = df["Rings"].round().clip(lower=1)

df.loc[2, "Height"] = np.nan
df.loc[20, "Height"] = 9.99
df = df[(df["Height"].isna()) | (df["Height"] < 1)].copy()
df[cols] = df[cols].fillna(df[cols].median())
X_train, X_val, y_train, y_val = train_test_split(
df[cols], df["Rings"], test_size=.2, random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)
pred = model.predict(X_val)

print("MSE:",np.sqrt(mean_squared_error(y_val,pred)))
print("MAE：", mean_absolute_error(y_val, pred))
print("R²：", r2_score(y_val, pred))

plt.scatter(y_val, pred, alpha=.7)
low,high = min(y_val.min(),pred.min()),max(y_val.max(),pred.max())
plt.plot([low, high], [low, high], "r--")
plt.xlabel("true Rings")
plt.ylabel("predict Rings")
plt.title("line result")
# 自动调整子图参数使之紧凑排列
plt.tight_layout()
plt.savefig("reports/linear_prediction.png", dpi=150)
plt.close()