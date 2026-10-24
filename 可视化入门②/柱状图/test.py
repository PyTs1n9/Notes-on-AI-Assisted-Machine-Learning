"""
柱状图 · 练习题
=================================
题目背景：
    某电商平台统计了大促期间 6 个品类的销售额（万元）。

任务要求：
    1. 绘制单组竖向柱状图，柱子宽度 0.6。
    2. 给每根柱子按“销售额高低”上色：销售额 ≥ 80 用红色 "#d62728"，
       其余用灰色 "#9e9e9e"（提示：用列表推导式逐根指定 color）。
    3. 在柱顶显示销售额数值，保留 1 位小数（提示：labels=[f"{v:.1f}" ...]）。
    4. 标题“大促期间各品类销售额”，y 轴标签“销售额（万元）”，y 轴范围 0~110。
    5. 只保留横向网格线，并置于柱子下方；隐藏上/右边框。
    6. 保存为 柱状图练习.png（dpi=150）。

进阶（可选）：
    在同一张图上再叠加一条“同比增长率”折线（用 twinx() 生成副坐标轴）。

提示：竖向柱状图用 ax.bar()，横向柱状图用 ax.barh()，不要混用。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

categories = ["手机", "电脑", "家电", "服饰", "美妆", "食品"]
sales = np.array([96.5, 88.2, 74.3, 61.8, 52.4, 83.7])

fig, ax = plt.subplots(figsize=(9, 5))

# ============ TODO 1 & 2：绘制柱状图并按阈值配色 ============
# 提示：colors = ["#d62728" if v >= 80 else "#9e9e9e" for v in sales]
pass

# ============ TODO 3：柱顶显示数值（1 位小数） ============
pass

# ============ TODO 4：标题与坐标轴设置 ============
pass

# ============ TODO 5：横向网格 + 隐藏边框 ============
pass

# ============ TODO 6：保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# colors = ["#d62728" if v >= 80 else "#9e9e9e" for v in sales]
# bars = ax.bar(categories, sales, width=0.6, color=colors,
#               edgecolor="white", linewidth=1.2)
#
# ax.bar_label(bars, labels=[f"{v:.1f}" for v in sales], padding=3, fontsize=10)
#
# ax.set_title("大促期间各品类销售额", fontsize=15, fontweight="bold")
# ax.set_ylabel("销售额（万元）")
# ax.set_ylim(0, 110)
#
# ax.grid(axis="y", linestyle=":", alpha=0.6)
# ax.set_axisbelow(True)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
#
# fig.tight_layout()
# fig.savefig(BASE / "柱状图练习.png", dpi=150)
# plt.show()
