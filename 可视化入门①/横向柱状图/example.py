"""
横向柱状图 · 示例
类别名字比较长、或者类别比较多时，把柱子横过来更好看。
函数从 bar 换成 barh，其余写法和柱状图完全一样。
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据
cities = ["北京", "上海", "广州", "深圳", "杭州"]
sales = [95, 88, 76, 82, 64]

# 2. 画横向柱状图：barh(类别, 数值)
plt.barh(cities, sales)

# 3. 标题和坐标轴（注意：现在数值在 x 轴，类别在 y 轴）
plt.title("各城市销售额")
plt.xlabel("销售额（万元）")
plt.ylabel("城市")

# 4. 保存图片，再显示
plt.savefig("横向柱状图示例.png")
plt.show()
