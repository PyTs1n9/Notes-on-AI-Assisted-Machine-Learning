import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import root_mean_squared_error

Path("dataset").mkdir(exist_ok=True)
Path("image").mkdir(exist_ok=True)
dataset_dir = Path("dataset")
img_dir = Path("image")
hour_dir = dataset_dir / "hour.csv"
cols = ["temp", "atemp", "hum", "windspeed", "hr", "workingday", "weathersit"]
df = pd.read_csv(hour_dir)
X = df[cols]
y = df["cnt"]


def rmse_cal(a, n):
	X_train, X_val, y_train, y_val = train_test_split(
		X, y, test_size=0.2, random_state=n
	)
	ridge = Ridge(alpha=a)
	ridge.fit(X_train, y_train)
	pred = ridge.predict(X_val)
	return root_mean_squared_error(y_val, pred)


print("alpha = 0.1, random_state = 1   时", f"RMSE = {rmse_cal(1.0, 1):.4f}")
print("alpha = 0.1, random_state = 10  时", f"RMSE = {rmse_cal(1.0, 10):.4f}")
print("alpha = 0.1, random_state = 20  时", f"RMSE = {rmse_cal(1.0, 20):.4f}")
print("alpha = 0.1, random_state = 42  时", f"RMSE = {rmse_cal(1.0, 42):.4f}")
print("alpha = 0.1, random_state = 100 时", f"RMSE = {rmse_cal(1.0, 100):.4f}")
# 为什么不同随机划分会得到不同结果：因为训练集和验证集划分不同，学到的数据和测试的数据不同，RMSE也不同



scores = cross_val_score(Ridge(alpha=1.0), X, y, cv=5, scoring="neg_mean_squared_error")
print("平均分: ", scores.mean().round(5))
print("标准差: ", scores.std().round(5))
print()
X_train, X_val, y_train, y_val = train_test_split(
	X, y, test_size=0.2, random_state=42
)
param_grid = {"alpha": [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(Ridge(), param_grid, cv=5, scoring="neg_mean_squared_error")
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)
best_params = grid.best_params_
print("alpha = best_params, random_state = 42 时", f"RMSE = {rmse_cal(best_params.get('alpha'), 100):.4f}")

default_model = Ridge(alpha=1.0).fit(X_train, y_train)
best_model = Ridge(alpha=100).fit(X_train, y_train)
default_pred = default_model.predict(X_val)
best_pred = best_model.predict(X_val)
default_rmse = root_mean_squared_error(y_val, default_pred)
best_rmse = root_mean_squared_error(y_val, best_pred)
print("默认 Ridge RMSE：", f"{default_rmse:.4f}")
print("最优 Ridge RMSE：", f"{best_rmse:.4f}")

alphas = np.array(
	grid.cv_results_["param_alpha"],
	dtype=float
)
n_splits = grid.n_splits_

# 每个 alpha 在每一折上的负 MSE
fold_mse = np.column_stack([
    -grid.cv_results_[f"split{i}_test_score"]
    for i in range(n_splits)
])

# 将每折 MSE 转换为 RMSE
fold_rmse = np.sqrt(fold_mse)

# 每个 alpha 的平均 RMSE 和标准差
cv_rmse = fold_rmse.mean(axis=1)
cv_std = fold_rmse.std(axis=0)

# 按 alpha 从小到大排序
order = np.argsort(alphas)

plt.figure(figsize=(7, 4))
plt.errorbar(
    alphas[order],
    cv_rmse[order],
    yerr=cv_std[order],
    marker="o",
    capsize=4
)

plt.xscale("log")
plt.xlabel("alpha")
plt.ylabel("Cross-validation RMSE")
plt.title("alpha and 5-fold CV RMSE")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(img_dir / "image.png")
plt.show()
