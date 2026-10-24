# 作用： 对 Ridge 做五折评分并转为正的 RMSE。
# 运行后看到： 五个正数和平均值

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

X = np.random.rand(30, 2)
y = X[:, 0] * .5 + X[:, 1] * .2

scores = cross_val_score(Ridge(alpha=1.0),X,y,cv=5,scoring="neg_mean_squared_error")
rmse = np.sqrt(-scores)
print("每折 RMSE：", rmse.round(3))
print("平均 RMSE：", rmse.mean().round(3))
