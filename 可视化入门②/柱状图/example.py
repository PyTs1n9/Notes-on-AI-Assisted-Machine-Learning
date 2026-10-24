"""
柱状图（Bar Chart）示例
=================================
适用场景：比较不同“类别”之间的数值大小，类别之间无先后顺序。

本示例要点：
1. bar() 绘制竖向柱状图，第一个参数是类别位置，第二个参数是高度
2. width 控制柱宽，color 可按数据大小做渐变配色
3. 用 ax.bar_label() 或 text() 在柱顶显示具体数值
4. 两组数据对比时使用“分组柱状图”，柱子的 x 位置需要错开
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 数据 ----------
subjects = ["语文", "数学", "英语", "物理", "化学", "生物"]
class_1 = np.array([82, 88, 79, 75, 81, 86])   # 一班平均分
class_2 = np.array([85, 84, 83, 78, 76, 83])   # 二班平均分

x = np.arange(len(subjects))   # 类别的数值位置：[0, 1, 2, 3, 4, 5]
width = 0.38                   # 柱宽（两组柱各占 0.38，合计 0.76，留出间隙）

fig, ax = plt.subplots(figsize=(9, 5))

# ---------- 2. 绘制分组柱状图 ----------
# 一班：向左偏移半个柱宽
bars1 = ax.bar(x - width / 2, class_1, width,
               label="一班", color="#4c72b0")

# 二班：向右偏移半个柱宽
bars2 = ax.bar(x + width / 2, class_2, width,
               label="二班", color="#dd8452")

# ---------- 3. 在柱顶标注数值 ----------
ax.bar_label(bars1, padding=2, fontsize=9, color="#333333")
ax.bar_label(bars2, padding=2, fontsize=9, color="#333333")

# ---------- 4. 完善图表元素 ----------
ax.set_title("期末各科平均分对比（一班 vs 二班）", fontsize=15, fontweight="bold")
ax.set_xlabel("科目", fontsize=11)
ax.set_ylabel("平均分", fontsize=11)
ax.set_xticks(x)                    # 刻度位置对齐到类别中心
ax.set_xticklabels(subjects)        # 刻度标签显示中文科目名
ax.set_ylim(0, 100)
ax.legend(loc="upper right", ncol=2)          # 两列图例
ax.grid(axis="y", linestyle=":", alpha=0.6)   # 只开横向网格
ax.set_axisbelow(True)                         # 网格置于柱子下方

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(BASE / "柱状图示例.png", dpi=150)
plt.show()
