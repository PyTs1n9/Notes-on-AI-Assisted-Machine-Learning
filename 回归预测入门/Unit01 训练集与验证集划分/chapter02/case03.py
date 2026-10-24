# 作用： 将 100 条样本按 80% 和 20% 划开。
# 运行后看到： 打印训练和验证的样本数。

import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(100).reshape(-1, 1)
y = X.ravel() * 2 + 1

X_train, X_val, y_train, y_val = train_test_split(
	X, y, test_size=0.2, random_state=42
)

print("训练数：", len(X_train), "验证数：", len(X_val))

