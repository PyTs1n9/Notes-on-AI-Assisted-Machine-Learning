"""
饼图（Pie Chart）示例
=================================
适用场景：
    展示“部分占整体”的比例关系，所有扇区的和必须为 100%。
    类别数建议 3~7 个，过多时应改用横向柱状图。

本示例要点：
1. pie() 的 sizes 会自动归一化，但业务上必须保证总和为 100%
2. explode 把某个扇区“抽离”出来做强调
3. autopct 显示百分比格式，pctdistance 控制百分比文字与圆心的距离
4. startangle 从 12 点钟方向开始绘制，符合阅读习惯
5. wedgeprops 可设置扇区边框，让相邻扇区更易区分
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 数据 ----------
brands = ["品牌A", "品牌B", "品牌C", "品牌D", "其他"]
share = np.array([34.5, 26.0, 18.2, 12.3, 9.0])   # 百分比，合计 100
colors = ["#2e75b6", "#ed7d31", "#a5a5a5", "#ffc000", "#c9c9c9"]

# 突出“品牌A”：第 0 个扇区向外偏移 0.08
explode = [0.08, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(7.5, 6.5))

# ---------- 2. 绘制饼图 ----------
wedges, texts, autotexts = ax.pie(
    share,
    labels=brands,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",            # 百分比格式：保留 1 位小数
    startangle=90,                # 从 12 点钟方向开始，顺时针绘制
    counterclock=False,
    pctdistance=0.65,             # 百分比文字距圆心 0.65 个半径
    labeldistance=1.12,           # 类别标签距圆心 1.12 个半径
    textprops={"fontsize": 11},
    wedgeprops={"edgecolor": "white", "linewidth": 2},  # 扇区白色分隔线
)

# 百分比文字设为白色加粗，提升可读性
for t in autotexts:
    t.set_color("white")
    t.set_fontweight("bold")
    t.set_fontsize(11)

# ---------- 3. 中心留白，做成“环形图”风格（可选） ----------
# 画一个白色圆盖住圆心，形成甜甜圈效果；若不需要请注释掉这两行
centre_circle = plt.Circle((0, 0), 0.42, fc="white")
ax.add_artist(centre_circle)
ax.text(0, 0, "市场份额\n2025", ha="center", va="center",
        fontsize=13, fontweight="bold", color="#333333")

# ---------- 4. 完善图表元素 ----------
ax.set_title("2025年智能手机品牌市场份额", fontsize=15, fontweight="bold", pad=18)
ax.axis("equal")     # 保证是正圆而不是椭圆

fig.tight_layout()
fig.savefig(BASE / "饼图示例.png", dpi=150)
plt.show()
