# 练习：运行手工例子；把一个预测数改得很离谱；
# 比较 RMSE 和 MAE变化；
# 再把同样计算用于 rings验证集。


import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

真实 = np.array([3, 5, 7, 9])
预测 = np.array([4, 4, 8, 10])
改预测 = np.array([4, 4, 8, 10000])

print("RMSE：", np.sqrt(mean_squared_error(真实, 预测)))
print("改 RMSE：", np.sqrt(mean_squared_error(真实, 改预测)))
print("MAE：", mean_absolute_error(真实, 预测))
print("改 MAE：", mean_absolute_error(真实, 改预测))
print("R²：", r2_score(真实, 预测))