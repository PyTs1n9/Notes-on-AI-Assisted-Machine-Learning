# 作用： 用手工预测值计算三个指标。
# 运行后看到： 控制台打印三个数字。

import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

真实 = np.array([3, 5, 7, 9])
预测 = np.array([4, 4, 8, 10])

print("RMSE：", np.sqrt(mean_squared_error(真实, 预测)))
print("MAE：", mean_absolute_error(真实, 预测))
print("R²：", r2_score(真实, 预测))