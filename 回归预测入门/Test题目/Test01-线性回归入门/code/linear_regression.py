from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

output_dir = Path(r"D:\Code\Python\人工智能基础\回归预测入门\Test题目\Test01-线性回归入门\output")
output_dir.mkdir(parents=True, exist_ok=True)
data = fetch_california_housing(as_frame=True)

print(data.frame.head(10))
print(data.frame.shape)
print(data.frame.columns.tolist())
print(data.frame.dtypes)
print(data.frame.describe())

cols = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]
X = data.frame[cols]
y = data.frame["MedHouseVal"]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_val)

df = pd.DataFrame(
    {
        "actual": np.asarray(y_val),
        "predicted": np.asarray(pred),
        "error": np.asarray(y_val) - np.asarray(pred),
    }
)

print(df.head(20).round(4))
csv_dir = output_dir / "predictions.csv"
df.to_csv(csv_dir, index=False, encoding="utf-8-sig")

def showimg(n,dataframe):
    plt.figure(figsize=(8, 6))
    plt.scatter(dataframe["actual"], dataframe["predicted"], alpha=0.5, s=15, label="result")

    limit_min = min(dataframe["actual"].min(), dataframe["predicted"].min())
    limit_max = max(dataframe["actual"].max(), dataframe["predicted"].max())
    plt.plot(
        [limit_min, limit_max],
        [limit_min, limit_max],
        "r--",
        label="y = x",
    )

    plt.xlabel("True")
    plt.ylabel("Pred")
    plt.title(f"California Housing Pred_{n}")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    img_dir = Path(r"D:\Code\Python\人工智能基础\回归预测入门\Test题目\Test01-线性回归入门\figures")
    img_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(img_dir / f"predictions_scatter_{n}.png", dpi=150)
    plt.show()

showimg(0,df)


cols_1 = ["MedInc"]
X_1 = data.frame[cols_1]
X_1train, X_1val, y_train, y_val = train_test_split(
    X_1, y, test_size=0.2, random_state=42
)
model_1 = LinearRegression()
model_1.fit(X_1train, y_train)
pred_1 = model_1.predict(X_1val)
df_1 = pd.DataFrame(
    {
        "actual": np.asarray(y_val),
        "predicted": np.asarray(pred_1),
        "error": np.asarray(y_val) - np.asarray(pred_1),
    }
)
showimg(1,df_1)

cols_2 = ["MedInc","HouseAge","AveRooms"]
X_2 = data.frame[cols_2]
X_2train, X_2val, y_train, y_val = train_test_split(
    X_2, y, test_size=0.2, random_state=42
)
model_2 = LinearRegression()
model_2.fit(X_2train, y_train)
pred_2 = model_2.predict(X_2val)
df_2 = pd.DataFrame(
    {
        "actual": np.asarray(y_val),
        "predicted": np.asarray(pred_2),
        "error": np.asarray(y_val) - np.asarray(pred_2),
    }
)
showimg(2,df_2)