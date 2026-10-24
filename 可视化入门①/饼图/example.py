"""
饼图 · 示例
饼图用来看“各部分占整体的比例”，各部分加起来必须是 100%。
类别不要太多，最好 3~6 个。
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：标签列表 + 占比列表，长度要一样
labels = ["房租", "餐饮", "交通", "娱乐"]
money = [3000, 2000, 800, 1200]     # 各项支出

# 2. 画饼图：pie(占比, labels=标签, autopct=百分比格式)
#    "%1.1f%%" 表示保留 1 位小数的百分比
plt.pie(money, labels=labels, autopct="%1.1f%%")

# 3. 标题（饼图不需要坐标轴标签）
plt.title("每月支出占比")

# 4. 保存图片，再显示
plt.savefig("饼图示例.png")
plt.show()
