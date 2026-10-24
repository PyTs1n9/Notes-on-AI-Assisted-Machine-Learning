# 作用： 创建 Ridge、拟合并预测。
# 运行后看到： 显示预测数值。

import numpy as np
from sklearn.linear_model import Ridge

# 为什么要用 float？ 因为机器学习模型（如 Ridge）的计算需要浮点数
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]], float)
y = np.array([5, 5, 11, 11], float)

model = Ridge(alpha=1.0)
model.fit(X, y)
print(model.predict([[5, 4]]))
