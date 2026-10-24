# 某城市共享单车运营部门希望利用 天气weathersit、日期和时段 等信息预测  某小时的共享单车需求量cnt  ，以提前进行车辆调度。
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

Path("../output").mkdir(exist_ok=True)
output_dir = Path("../output")
Path("../figures").mkdir(exist_ok=True)
figures_dir = Path("../figures")
dataset_dir = Path("../dataset")

df = pd.read_csv(dataset_dir / "hour.csv")

X = df[["yr", "hr", "holiday", "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"]]
y = df["cnt"]

X_train, X_val, y_train, y_val = train_test_split(
	X, y, test_size=0.2, random_state=42
)

encoder = OneHotEncoder(sparse_output=False)
enc_cols = np.array([df["season"], df["mnth"], df["weekday"]])
encoded = encoder.fit_transform(enc_cols)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
pred_lr = model_lr.predict(X_val)

model_ri = Ridge()
model_ri.fit(X_train, y_train)
pred_ri = model_ri.predict(X_val)

model_la = Lasso()
model_la.fit(X_train, y_train)
pred_la = model_la.predict(X_val)

predictions = pd.DataFrame({
	"LinearRegression": pred_lr,
	"Ridge": pred_ri,
	"Lasso": pred_la
})
predictions.to_csv(output_dir / "predictions.csv", index=False)


def func_cal(pred):
	MAE = mean_absolute_error(y_val, pred)
	RMSE = root_mean_squared_error(y_val, pred)
	R2 = r2_score(y_val, pred)
	return MAE, RMSE, R2


model_metrics = pd.DataFrame([
	{"model": "LinearRegression", "MAE": func_cal(pred_lr)[0], "RMSE": func_cal(pred_lr)[1],
	 "R2": func_cal(pred_lr)[2]},
	{"model": "Ridge", "MAE": func_cal(pred_ri)[0], "RMSE": func_cal(pred_ri)[1], "R2": func_cal(pred_ri)[2]},
	{"model": "Lasso", "MAE": func_cal(pred_la)[0], "RMSE": func_cal(pred_la)[1], "R2": func_cal(pred_la)[2]},
])
model_metrics.to_csv(output_dir / "model_metrics.csv", index=False)

scores_lr = cross_val_score(LinearRegression(), X, y, cv=5, scoring="neg_mean_absolute_error")
score_lr_mean = -scores_lr.mean().round(5)
scores_ri = cross_val_score(Ridge(alpha=1.0), X, y, cv=5, scoring="neg_mean_absolute_error")
scores_ri_mean = -scores_ri.mean().round(5)
scores_la = cross_val_score(Lasso(max_iter=10000), X, y, cv=5, scoring="neg_mean_absolute_error")
scores_la_mean = -scores_la.mean().round(5)

model_list = [
	{
		"name": "LinearRegression",
		"model": LinearRegression(),
		"params": {}
	},
	{
		"name": "Ridge",
		"model": Ridge(),
		"params": {"alpha": [0.01, 0.1, 1, 10, 100]}
	},
	{
		"name": "Lasso",
		"model": Lasso(),
		"params": {"max_iter": [10000]}
	}
]
results = []
for item in model_list:
	name = item["name"]
	model = item["model"]
	params = item["params"]
	grid = GridSearchCV(estimator=model, param_grid=params, cv=5, scoring="neg_mean_squared_error")
	grid.fit(X_train, y_train)

	best_score = grid.best_score_
	best_params = grid.best_params_
	best_estimator = grid.best_estimator_
	cv_result = grid.cv_results_

	results.append({
		"name": name,
		"best_score": best_score,
		"best_params": best_params,
		"best_model": best_estimator,
		"cv_result": cv_result
	})

# 	print(f"{name}模型：")
# 	print(f"最优参数：{best_params}")
# 	print(f"最优分数：{best_score}")
#
# print()
#
# results.sort(key=lambda x: x["best_score"], reverse=True)
# print("最优模型：", results[0]["name"])
# print("最优模型参数：", results[0]["best_params"])

cv_results = pd.DataFrame(cv_result).T
cv_results.to_csv(output_dir / "cv_results.csv")

