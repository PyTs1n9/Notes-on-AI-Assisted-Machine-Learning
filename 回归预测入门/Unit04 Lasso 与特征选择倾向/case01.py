# 作用： 拟合 Lasso 并读取系数。
# 运行后看到： 打印每列系数，有些可能接近 0

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso

X = np.array([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]], float)
y = np.array([2, 4, 6, 8, 10], float)
# max_iter 增大迭代上限以减少未收敛提醒
model = make_pipeline(StandardScaler(),Lasso(alpha=0.1,max_iter=10000))
model.fit(X,y)
print(model.named_steps["lasso"].coef_)