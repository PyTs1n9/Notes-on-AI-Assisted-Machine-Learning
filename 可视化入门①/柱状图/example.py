"""
柱状图 · 示例
柱状图用来比较“不同类别的大小”，比如各科平均分。

画图四步：数据 → 画图 → 标题和坐标轴 → 保存并显示
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：类别列表 + 数值列表，长度要一样
subjects = ["语文", "数学", "英语", "物理", "化学"]
scores = [82, 88, 79, 75, 81]

# 2. 画柱状图：bar(类别, 数值)
plt.bar(subjects, scores)

# 3. 标题和坐标轴
plt.title("各科平均分")
plt.xlabel("科目")
plt.ylabel("分数")

# 4. 保存图片，再显示
plt.savefig("柱状图示例.png")
plt.show()
