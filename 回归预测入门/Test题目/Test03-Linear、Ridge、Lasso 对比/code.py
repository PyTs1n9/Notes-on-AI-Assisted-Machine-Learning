from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

dataset_dir = Path("dataset")
Path("output").mkdir(exist_ok=True)
output_dir = Path("output")
df = pd.read_csv(dataset_dir / "winequality-white.csv", sep=';')

X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
        "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
        "pH", "sulphates", "alcohol", ]]
y = df["quality"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
pred_lr = model_lr.predict(X_val)

model_ri = Ridge(alpha=1.0)
model_ri.fit(X_train, y_train)
pred_rg = model_ri.predict(X_val)

model_la = Lasso(alpha=.1, max_iter=10000)
model_la.fit(X_train, y_train)
pred_la = model_la.predict(X_val)


def metrics(pred):
	return {
		"MAE": mean_absolute_error(y_val, pred),
		"RMSE": root_mean_squared_error(y_val, pred),
		"R2": r2_score(y_val, pred)
	}


df = pd.DataFrame({
	"LinearRegression": metrics(pred_lr),
	"Ridge": metrics(pred_rg),
	"Lasso": metrics(pred_la),
}).round(5)

df.to_csv(output_dir / "model_metrics.csv", index=False)

coef_df = pd.DataFrame({
	"Feature": X.columns,
	"LinearRegression": model_lr.coef_,
	"Ridge": model_ri.coef_,
	"Lasso": model_la.coef_,
})

coef_df.to_csv(output_dir / "model_coefficients.csv", index=False)

fig, ax = plt.subplots(figsize=(12, 6))
coef_df.set_index("Feature").plot.bar(ax=ax)
ax.set_ylabel("coef")
ax.set_title("Coef Comparison")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig(output_dir / "coeff_table.png", dpi=150)
plt.show()

alphas = [0.01, 0.1, 1, 10, 100]
results = []

def models(model_class, alpha, model_name):
	model = model_class(alpha=alpha)
	model.fit(X_train, y_train)
	predict = model.predict(X_val)
	return predict, {
        "Model": model_name,
        "alpha": alpha,
        "MAE": mean_absolute_error(y_val, predict),
        "RMSE": root_mean_squared_error(y_val, predict),
        "R2": r2_score(y_val, predict)
    }

for alpha in alphas:
	_, scores = models(Ridge, alpha, "Ridge")
	results.append(scores)
	print(f"Ridge alpha={alpha}: {scores}")

for alpha in alphas:
	_, scores = models(Lasso, alpha, "Lasso")
	results.append(scores)
	print(f"Lasso alpha={alpha}: {scores}")

results_df = pd.DataFrame(results)
results_df.to_csv(output_dir / "alpha_comparison.csv", index=False)

fig, ax = plt.subplots()
for model in ["Ridge", "Lasso"]:
	data = results_df[results_df["Model"] == model]
	ax.plot(data["alpha"], data["RMSE"], marker="o", label=model)
ax.set_xscale("log")
ax.set_xlabel("alpha")
ax.set_ylabel("RMSE")
ax.set_title("Alpha vs RMSE")
ax.legend()
plt.savefig(output_dir / "alpha_rmse_curve.png", dpi=150)
plt.show()