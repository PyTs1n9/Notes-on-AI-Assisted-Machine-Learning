# 作用： 学习一个简单直线关系，再预测新输入。
# 运行后看到： 对输入 6 的预测接近 13。

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
model = LinearRegression()
model.fit(X,y)
print(model.predict([[6]]))
