"""
散点图 · 示例
散点图用来看“两个数值之间有没有关系”，比如学习时长和成绩。
每个点代表一条数据：(x, y)。
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：两个数值列表，长度要一样
hours = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7]        # 每周学习时长
scores = [55, 58, 62, 65, 70, 68, 75, 80, 78, 88]   # 考试成绩

# 2. 画散点图：scatter(x, y)
plt.scatter(hours, scores)

# 3. 标题和坐标轴
plt.title("学习时长与考试成绩")
plt.xlabel("每周学习时长（小时）")
plt.ylabel("成绩（分）")

# 4. 保存图片，再显示
plt.savefig("散点图示例.png")
plt.show()
