"""
横向柱状图（Horizontal Bar Chart）示例
=================================
适用场景：
    1. 类别名称较长（如城市名、商品名），竖向柱状图会挤在一起
    2. 类别数量较多（一般 > 8 个），横向排列更易读
    3. 需要按数值排序展示“排行榜”

本示例要点：
1. barh() 与 bar() 参数顺序一致，只是 x/y 含义互换
2. 排序技巧：先按数值升序排列，配合 barh 自下而上的绘制顺序，
   使最大值出现在最上方（如果要最大值在顶部，就用升序数据 + barh）
3. ax.bar_label() 在柱子末端显示数值，配合 padding 避免压线
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 数据 ----------
cities = ["深圳", "上海", "北京", "杭州", "广州", "成都", "南京", "武汉", "西安", "苏州"]
gmv = np.array([186, 245, 233, 158, 152, 121, 108, 96, 88, 132])  # 单位：亿元

# ---------- 2. 按数值升序排序 ----------
# barh 是从下往上画的，所以升序排列会让最大值出现在最上方
order = np.argsort(gmv)
cities_sorted = [cities[i] for i in order]
gmv_sorted = gmv[order]

fig, ax = plt.subplots(figsize=(9, 6))

# ---------- 3. 绘制横向柱状图 ----------
bars = ax.barh(cities_sorted, gmv_sorted,
               height=0.62,
               color=plt.cm.Blues(np.linspace(0.35, 0.95, len(gmv_sorted))),
               edgecolor="white")

# ---------- 4. 柱端标注数值 ----------
ax.bar_label(bars, labels=[f"{v} 亿" for v in gmv_sorted],
             padding=4, fontsize=9.5, color="#333333")

# ---------- 5. 完善图表元素 ----------
ax.set_title("2025年各城市 GMV 排名（单位：亿元）", fontsize=15, fontweight="bold", pad=12)
ax.set_xlabel("GMV（亿元）", fontsize=11)
ax.set_xlim(0, 285)
ax.grid(axis="x", linestyle=":", alpha=0.6)
ax.set_axisbelow(True)

# 横向图通常隐藏右侧和上方边框，并去掉 y 轴刻度线
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="y", length=0)     # 去掉 y 轴小刻度线

fig.tight_layout()
fig.savefig(BASE / "横向柱状图示例.png", dpi=150)
plt.show()
