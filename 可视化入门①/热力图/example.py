"""
热力图 · 示例
热力图用“颜色深浅”表示数字大小，适合二维表格数据：
比如 星期 × 时段 的客流量、不同变量的相关系数。

数据是一个二维列表（列表里再放列表），行数和列数要整齐。
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据：4 行 × 5 列，每个数字代表一个格子的颜色深浅
data = [
    [20, 35, 30, 45, 25],    # 周一
    [22, 38, 33, 48, 27],    # 周二
    [25, 40, 36, 52, 30],    # 周三
    [30, 50, 45, 60, 38],    # 周四
]

# 2. 画热力图：imshow(二维数据)
plt.imshow(data)
plt.colorbar()      # 右侧颜色条，说明颜色对应的数值

# 3. 坐标轴刻度：range(列数) 对应每个列的位置
plt.xticks(range(5), ["8点", "10点", "12点", "14点", "16点"])
plt.yticks(range(4), ["周一", "周二", "周三", "周四"])
plt.title("不同时段的客流量")

# 4. 保存图片，再显示
plt.savefig("热力图示例.png")
plt.show()
