# 练习：使用rings 数据；
# 用 StandardScaler 标准化；
# 先拟合 scaler 再变换训练和验证数据；
# 对比 Ridge 和 Linear的三个指标。
# 真实应用可把标准化和模型放进 Pipeline，确保交叉验证时每折只从训练折学习尺度。
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline

# 使用 Test02-Abalone 回归评价指标 中的 dataset/abalone.csv
dataset_dir = Path("dataset")
data_dir = dataset_dir / "abalone.csv"

# Sex 是字符串，需要编码（如 OneHot 或 LabelEncoder）
# Ridge 推荐用 OneHot
# 原因：LabelEncoder 会暗示 0 < 1 < 2，但 M、F、I 之间没有大小关系，会让模型误以为有数值大小关系。
df = pd.read_csv(data_dir)

X_num = df[["Length", "Diameter", "Height",
            "Whole weight", "Shucked weight", "Viscera weight", "Shell weight"]]
X_sex = df[["Sex"]].values
enc = OneHotEncoder(sparse_output=False)
X_sex_encoded = enc.fit_transform(X_sex)

X = np.hstack([X_num, X_sex_encoded])
y = df["Rings"]

# ① 数据划分
X_train, X_val, y_train, y_val = train_test_split(
	X, y, test_size=0.2, random_state=42)

# ② 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# ③ 模型训练
# alpha越大，系数越小，模型简单稳定，偏差大，欠拟合
# alpha越小，越接近LinearRegression，拟合更灵活，可能过拟合，=0等价与普通线性回归
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
lr = LinearRegression()
lr.fit(X_train, y_train)

# ④ 模型预测
y_pred_ridge = ridge.predict(X_val)
y_pred_lr = lr.predict(X_val)

# ⑤ 指标对比
print("Ridge:")
print(f"MSE: {mean_squared_error(y_val, y_pred_ridge):.4f}")
print(f"MAE: {mean_absolute_error(y_val, y_pred_ridge):.4f}")
print(f"R2: {r2_score(y_val, y_pred_ridge):.4f}")

print("Lr:")
print(f"MSE: {mean_squared_error(y_val, y_pred_lr):.4f}")
print(f"MAE: {mean_absolute_error(y_val, y_pred_lr):.4f}")
print(f"R2: {r2_score(y_val, y_pred_lr):.4f}")

# ⑥管道
pipe = Pipeline([
	("scaler", StandardScaler()),
	("model", Ridge(alpha=1.0))
])

# ⑦ 交叉验证
scores = cross_val_score(pipe, X, y, cv=5, scoring="r2")

print(f"每折 R2: {scores}")
print(f"平均 R2: {scores.mean():.4f} ± {scores.std():.4f}")
