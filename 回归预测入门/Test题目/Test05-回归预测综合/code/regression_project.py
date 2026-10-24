import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, KFold, cross_validate, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

project_dir = Path(__file__).resolve().parents[1]
output_dir = project_dir / "output"
figures_dir = project_dir / "figures"
Path(output_dir).mkdir(exist_ok=True)
Path(figures_dir).mkdir(exist_ok=True)
dataset_dir = Path(os.environ.get("BIKE_DATASET_DIR", project_dir / "dataset"))
if not (dataset_dir / "hour.csv").exists():
    dataset_dir = Path(r"D:\Code\Python\人工智能基础\回归预测入门\Test题目\Test05-回归预测综合\dataset")


df = pd.read_csv(dataset_dir / "hour.csv")
print("数据形状：", df.shape)
print("缺失值：", int(df.isna().sum().sum()), "重复行：", int(df.duplicated().sum()))
print(df["cnt"].describe())

df = df.drop(["instant", "casual", "registered"], axis=1)
df["dteday"] = pd.to_datetime(df["dteday"])
df["weekday"] = df["dteday"].dt.weekday
df["is_weekend"] = (df["weekday"] >= 5).astype(int)
df = df.drop("dteday", axis=1)
X = df.drop("cnt", axis=1)
y = df["cnt"]
numeric_features = ["temp", "atemp", "hum", "windspeed"]
categorical_features = ["season", "yr", "mnth", "hr", "holiday", "workingday", "weekday", "weathersit", "is_weekend"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features)
])

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# LinearRegression。
pipe_lr = make_pipeline(preprocessor, LinearRegression())
# Ridge。
pipe_ri = make_pipeline(preprocessor, Ridge(alpha=1.0))
# Lasso。
pipe_la = make_pipeline(preprocessor, Lasso(alpha=1.0, max_iter=20000))
models = {"LinearRegression": pipe_lr, "Ridge": pipe_ri, "Lasso": pipe_la}

predictions = pd.DataFrame({"row_index": X_val.index, "actual": y_val.to_numpy()})
result_list = []
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_val)
    predictions[name] = pred
    result_list.append({
        "model": name,
        "MAE": round(mean_absolute_error(y_val, pred), 3),
        "RMSE": round(np.sqrt(mean_squared_error(y_val, pred)), 3),
        "R2": round(r2_score(y_val, pred), 3)
    })
print(result_list)
df_result = pd.DataFrame(result_list).set_index("model")
print(df_result)

# 五折交叉验证。
cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_rows = []
scoring = {"MAE": "neg_mean_absolute_error", "RMSE": "neg_root_mean_squared_error", "R2": "r2"}
for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=cv, scoring=scoring)
    for fold in range(5):
        cv_rows.append({"model": name, "source": "five_fold_cv", "fold": fold+1, "alpha": np.nan,
                        "MAE": -scores["test_MAE"][fold], "RMSE": -scores["test_RMSE"][fold],
                        "R2": scores["test_R2"][fold], "rank": np.nan})

# Ridge参数搜索。
ridge_grid = GridSearchCV(make_pipeline(preprocessor, Ridge()),
    {"ridge__alpha": [0.01, 0.1, 1.0, 10.0, 100.0]},
    cv=cv, scoring=scoring, refit="MAE", return_train_score=False)
ridge_grid.fit(X_train, y_train)

# Lasso参数搜索。
lasso_grid = GridSearchCV(make_pipeline(preprocessor, Lasso(max_iter=20000)),
    {"lasso__alpha": [0.01, 0.1, 1.0, 10.0]},
    cv=cv, scoring=scoring, refit="MAE", return_train_score=False)
lasso_grid.fit(X_train, y_train)

for name, grid, key in [("Ridge", ridge_grid, "ridge__alpha"), ("Lasso", lasso_grid, "lasso__alpha")]:
    table = pd.DataFrame(grid.cv_results_)
    for i, row in table.iterrows():
        cv_rows.append({"model": name, "source": "alpha_search", "fold": np.nan, "alpha": row["param_"+key],
                        "MAE": -row["mean_test_MAE"],
                        "RMSE": -row["mean_test_RMSE"],
                        "R2": row["mean_test_R2"], "rank": row["rank_test_MAE"]})

cv_results = pd.DataFrame(cv_rows)
cv_results.to_csv(output_dir / "cv_results.csv", index=False)

candidate_scores = {
    "LinearRegression": -cross_validate(pipe_lr, X_train, y_train, cv=cv, scoring="neg_mean_absolute_error")["test_score"].mean(),
    "Ridge": -ridge_grid.best_score_,
    "Lasso": -lasso_grid.best_score_
}
final_name = min(candidate_scores, key=candidate_scores.get)
final_model = {"LinearRegression": pipe_lr, "Ridge": ridge_grid.best_estimator_,
               "Lasso": lasso_grid.best_estimator_}[final_name]
final_pred = final_model.predict(X_val)
predictions["final_model"] = final_pred
predictions["residual"] = y_val.to_numpy() - final_pred
predictions.to_csv(output_dir / "predictions.csv", index=False)
df_result.reset_index().to_csv(output_dir / "model_metrics.csv", index=False)

# 三模型指标比较图。
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, metric in zip(axes, ["MAE", "RMSE", "R2"]):
    ax.bar(df_result.index, df_result[metric], color=["#4C78A8", "#F58518", "#54A24B"])
    ax.set_title(metric)
    ax.tick_params(axis="x", rotation=20)
fig.tight_layout()
fig.savefig(figures_dir / "model_compare.png", dpi=150)
plt.close(fig)

# 真实值—预测值图。
plt.figure(figsize=(6, 6))
plt.scatter(y_val, final_pred, s=10, alpha=0.35, color="#4C78A8")
lo, hi = min(y_val.min(), final_pred.min()), max(y_val.max(), final_pred.max())
plt.plot([lo, hi], [lo, hi], "r--", label="Ideal")
plt.xlabel("Actual"); plt.ylabel("Predicted"); plt.title(f"{final_name}: Actual vs Predicted"); plt.legend()
plt.tight_layout(); plt.savefig(figures_dir / "prediction.png", dpi=150); plt.close()

# 残差图。
residual = y_val.to_numpy() - final_pred
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].hist(residual, bins=40, color="#4C78A8", edgecolor="white")
axes[0].set_title("Residual Histogram"); axes[0].set_xlabel("Actual - Predicted")
axes[1].scatter(final_pred, residual, s=10, alpha=0.35, color="#F58518")
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set_title("Residual vs Predicted"); axes[1].set_xlabel("Predicted"); axes[1].set_ylabel("Residual")
fig.tight_layout(); fig.savefig(figures_dir / "residual.png", dpi=150); plt.close(fig)

# 不同alpha对比图。
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, name in zip(axes, ["Ridge", "Lasso"]):
    part = cv_results[(cv_results["model"] == name) & (cv_results["source"] == "alpha_search")]
    ax.plot(part["alpha"], part["MAE"], marker="o")
    ax.set_xscale("log"); ax.set_title(f"{name} Alpha Comparison")
    ax.set_xlabel("alpha"); ax.set_ylabel("Mean CV MAE")
fig.tight_layout(); fig.savefig(figures_dir / "alpha_compare.png", dpi=150); plt.close(fig)

final_metric = {"MAE": mean_absolute_error(y_val, final_pred),
                "RMSE": np.sqrt(mean_squared_error(y_val, final_pred)),
                "R2": r2_score(y_val, final_pred)}
print("最优Ridge参数：", ridge_grid.best_params_)
print("最优Lasso参数：", lasso_grid.best_params_)
print("五折平均MAE：", candidate_scores)
print("最终模型：", final_name)
print("验证集指标：", final_metric)

