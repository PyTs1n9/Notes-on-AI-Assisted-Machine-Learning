"""
横向柱状图 · 练习题
=================================
题目背景：
    一份编程语言流行度调查结果（百分比，共 8 种语言）。

任务要求：
    1. 用 barh() 绘制横向柱状图，柱宽（height）设为 0.55。
    2. 按流行度从高到低排列，让最流行的语言显示在最上方。
       （提示：np.argsort 得到升序索引；barh 自下而上绘制，升序数据即最大值在顶）
    3. 所有柱子使用统一颜色 "#2a9d8f"，边框白色。
    4. 在柱子末端显示“XX%”格式的数值（保留 1 位小数）。
    5. 标题“编程语言流行度调查”，x 轴标签“占比（%）”，x 轴范围 0~40。
    6. 打开 x 方向网格并置于柱下，隐藏上/右边框，去掉 y 轴刻度线。
    7. 保存为 横向柱状图练习.png（dpi=150）。

易错点提醒：
    - barh 的第一个参数是“类别”，第二个是“长度”，顺序与 bar 相同，
      但 x 轴表示数值、y 轴表示类别
    - 忘记排序会导致图形杂乱，排行榜类图表必须排序
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

languages = ["Python", "Java", "JavaScript", "C++", "Go", "Rust", "C#", "PHP"]
share = np.array([28.6, 21.3, 18.9, 12.4, 9.7, 6.2, 8.1, 4.3])

fig, ax = plt.subplots(figsize=(9, 6))

# ============ TODO 1 & 2：排序并绘制横向柱状图 ============
pass

# ============ TODO 4：柱端显示百分比 ============
pass

# ============ TODO 3 & 5：颜色、标题、坐标轴 ============
pass

# ============ TODO 6：网格与边框处理 ============
pass

# ============ TODO 7：保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# order = np.argsort(share)                 # 升序索引
# langs_sorted = [languages[i] for i in order]
# share_sorted = share[order]
#
# bars = ax.barh(langs_sorted, share_sorted, height=0.55,
#                color="#2a9d8f", edgecolor="white")
#
# ax.bar_label(bars, labels=[f"{v:.1f}%" for v in share_sorted],
#              padding=4, fontsize=10)
#
# ax.set_title("编程语言流行度调查", fontsize=15, fontweight="bold")
# ax.set_xlabel("占比（%）")
# ax.set_xlim(0, 40)
#
# ax.grid(axis="x", linestyle=":", alpha=0.6)
# ax.set_axisbelow(True)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# ax.tick_params(axis="y", length=0)
#
# fig.tight_layout()
# fig.savefig(BASE / "横向柱状图练习.png", dpi=150)
# plt.show()
