"""
折线图 · 示例
折线图用来看“变化趋势”，比如一周的气温、一年的销量。

画图四步：数据 → 画图 → 标题和坐标轴 → 保存并显示
"""

import matplotlib.pyplot as plt

# 让中文正常显示（Windows 用微软雅黑）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：x 轴和 y 轴各一个列表，长度要一样
days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
beijing = [18, 20, 17, 22, 25, 24, 21]      # 北京最高气温
shanghai = [22, 23, 21, 25, 27, 26, 24]     # 上海最高气温

# 2. 画折线：plot(x, y, label=图例名字)
plt.plot(days, beijing, label="北京")
plt.plot(days, shanghai, label="上海")

# 3. 标题和坐标轴
plt.title("一周最高气温")
plt.xlabel("星期")
plt.ylabel("温度（℃）")
plt.legend()      # 显示图例（画了两条线才需要）
plt.grid()        # 显示网格，方便读数

# 4. 保存图片，再显示
plt.savefig("折线图示例.png")
plt.show()
