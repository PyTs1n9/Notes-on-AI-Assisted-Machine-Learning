"""
直方图 · 示例
直方图用来看“一堆数字的分布”：集中在哪个区间、有没有偏大偏小。
x 轴是一段段区间（叫箱子 bins），y 轴是落在该区间的个数。

注意：柱状图比类别大小，直方图看数值分布，两者不一样。
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：100 名学生的成绩（用随机数模拟，成绩≈正态分布）
scores = np.random.normal(70, 10, 100)   # 平均 70 分，波动 10 分，共 100 个

# 2. 画直方图：hist(数据, bins=分成几段)
plt.hist(scores, bins=10)

# 3. 标题和坐标轴
plt.title("100名学生成绩分布")
plt.xlabel("分数")
plt.ylabel("人数")

# 4. 保存图片，再显示
plt.savefig("直方图示例.png")
plt.show()
