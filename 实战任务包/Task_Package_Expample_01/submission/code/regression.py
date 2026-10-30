import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import (
	train_test_split, cross_val_score, KFold, GridSearchCV
)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import (
	LinearRegression, Lasso, Ridge
)
from sklearn.metrics import (
	mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score
)

plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('../data_outputs/hour_clean.csv', encoding='utf-8-sig')

drop_list = ["cnt", "casual", "registered", "instant"]
X = df.drop(columns=drop_list)
y = df["cnt"]

X['dteday'] = pd.to_datetime(X['dteday'], errors='coerce')
X['date_year'] = X['dteday'].dt.year
X['date_month'] = X['dteday'].dt.month
X['date_day'] = X['dteday'].dt.day

X = X.drop('dteday', axis=1)
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
	'ols': LinearRegression(),
	'Ridge': Ridge(alpha=1.0),
	'Lasso': Lasso(alpha=1.0, max_iter=10000)
}

rows_metrics = []
pred_df = pd.DataFrame({'y_true': y_test.values})
for name, m in models.items():
	m.fit(X_train_scaled, y_train)
	pred = m.predict(X_test_scaled)
	mae = mean_absolute_error(y_test, pred)
	mse = mean_squared_error(y_test, pred)
	rmse = root_mean_squared_error(y_test, pred)
	r2 = r2_score(y_test, pred)
	rows_metrics.append({
		'Model': name,
		'MAE': mae,
		'MSE': mse,
		'RMSE': rmse,
		'R2': r2
	})
	pred_df[f'{name}_pred'] = pred

regression_metrics = pd.DataFrame(rows_metrics)
regression_metrics.to_csv('../metrics/regression_metrics.csv', encoding='utf-8-sig', index=False)
regression_predictions = pd.DataFrame(pred_df)
regression_predictions.to_csv('../data_outputs/regression_predictions.csv', encoding='utf-8-sig', index=False)

models = {'Ridge': Ridge(), 'Lasso': Lasso()}
alpha_list = [0.01, 0.1, 1, 10, 100]
cv = KFold(n_splits=5, shuffle=True, random_state=42)
for a in alpha_list:
	ridge_score = cross_val_score(Ridge(alpha=a), X_train_scaled, y_train, cv=cv)
	print(f'Ridge alpha={a:<6} 平均CV分数: {ridge_score.mean():.4f}')
for a in alpha_list:
	lasso_score = cross_val_score(Lasso(alpha=a), X_train_scaled, y_train, cv=cv)
	print(f'Lasso alpha={a:<6} 平均CV分数: {lasso_score.mean():.4f}')

gs = GridSearchCV(Ridge(), {'alpha': alpha_list}, cv=cv)
gs.fit(X_train_scaled, y_train)
print('Ridge最优alpha参数：', gs.best_params_)
print('Ridge平均CV分数：', gs.best_score_)
gs = GridSearchCV(Lasso(), {'alpha': alpha_list}, cv=cv)
gs.fit(X_train_scaled, y_train)
print('Lasso最优alpha参数：', gs.best_params_)
print('Lasso平均CV分数：', gs.best_score_)

# A2-5,A2-6 不会写了
