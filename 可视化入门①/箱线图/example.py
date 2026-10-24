"""
箱线图 · 示例
箱线图用来看“一组数据的分部情况”，还能顺便发现异常值（离群点）。
一个箱子包含：最小值、下四分位数、中位数、上四分位数、最大值。
想同时比较好几组数据时，一图排开最直观。
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：三组数据，每组一个列表，把它们放进一个大列表里
np.random.seed(0)     # 固定随机结果，保证每次画出来一样
class_a = np.random.normal(75, 8, 50)
class_b = np.random.normal(82, 6, 50)
class_c = np.random.normal(70, 12, 50)

data = [class_a, class_b, class_c]

# 2. 画箱线图：boxplot(数据)
plt.boxplot(data)

# 3. 标题和坐标轴
plt.title("三个班的成绩分布")
plt.xlabel("班级")
plt.ylabel("分数")
# 默认横轴标 1、2、3，对应 data 里的第 1、2、3 组
plt.xticks([1, 2, 3], ["一班", "二班", "三班"])

# 4. 保存图片，再显示
plt.savefig("箱线图示例.png")
plt.show()
