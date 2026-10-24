from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, r2_score

dataset_dir = Path(r"dataset")
imgae_dir = Path(r"image").mkdir(exist_ok=True)
output_dir = Path(r"output").mkdir(exist_ok=True)
df = pd.read_csv(dataset_dir / "abalone.csv")
print(df)

X = df[["Length", "Diameter", "Height",
        "Whole weight", "Shucked weight", "Viscera weight", "Shell weight"]]
y = df["Rings"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_val)

MAE = mean_absolute_error(y_val, pred)
MSE = mean_squared_error(y_val, pred)
RMSE = root_mean_squared_error(y_val, pred)
R2 = r2_score(y_val, pred)

metrics_csv = pd.DataFrame({
	"MAE": [MAE],
	"MSE": [MSE],
	"RMSE": [RMSE],
	"R2": [R2],
})
metrics_csv = metrics_csv.round(3)
metrics_csv.to_csv("output/metrics.csv", index=False)

results = pd.DataFrame({
	"真实值": y_val,
	"预测值": pred,
	"绝对误差": abs(y_val - pred)
})
results = results.round(3)
results.to_csv("output/results.csv", index=False)
sample = results.head(5)
sample_mae = sample["绝对误差"].mean()
print(f"手工计算 {sample_mae:.3f}")
print(f"Python计算 {MAE:.3f}")
# 预测最准确的 10 条；
print(results.nsmallest(10, "绝对误差").describe())
# 预测误差最大的 10 条。
print(results.nlargest(10, "绝对误差").describe())

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].scatter(y_val, pred, alpha=0.5, s=10)
axes[0].plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--')
axes[0].set_xlabel("val")
axes[0].set_ylabel("pred")
axes[0].set_title("val & pred")

residuals = pred - y_val
axes[1].scatter(pred, residuals, alpha=0.5, s=10)
axes[1].axhline(y=0, color='r', linestyle='--')
axes[1].set_xlabel("pred")
axes[1].set_ylabel("residuals")
axes[1].set_title("pred & residuals")

axes[2].hist(abs(y_val - pred), bins=30, edgecolor='black')
axes[2].set_xlabel("ae")
axes[2].set_title("ae table")
plt.savefig("image/analysis_plots.png", dpi=150)

pred_tampered = pred.copy()
# 人为把 5 条预测结果增加 20。
pred_tampered[:5] += 20

mae_new = mean_absolute_error(y_val, pred_tampered)
rmse_new = root_mean_squared_error(y_val, pred_tampered)

print(f"MAE: {MAE:.3f}, RMSE: {RMSE:.3f}")
print(f"+20: MAE: {mae_new:.3f}, RMSE: {rmse_new:.3f}")
print(f"MAE增幅:  {mae_new - MAE:.3f}")
print(f"RMSE增幅: {rmse_new - RMSE:.3f}")

# 提高任务
X = df[["Sex", "Length", "Diameter", "Height",
        "Whole weight", "Shucked weight", "Viscera weight", "Shell weight"]]
X_encoded = pd.get_dummies(X, columns=["Sex"])
y = df["Rings"]
X_train,X_val,y_train,y_val = train_test_split(X_encoded,y,test_size=0.2,random_state=42)
models = LinearRegression()
models.fit(X_train, y_train)
pred = models.predict(X_val)
mse = mean_squared_error(y_val, pred)
print(f"提高任务均方误差 (MSE): {mse:.2f}")
# 7. 查看编码后的特征列
print("\n编码后的特征列:")
print(X_encoded.columns.tolist())