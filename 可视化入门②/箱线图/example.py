"""
箱线图（Box Plot）示例
=================================
适用场景：
    比较多个组别数据的“分布差异”，一次看清中位数、四分位距（IQR）和异常值。

箱线图的五个关键量（五数概括）：
    - 下边缘（须）：Q1 - 1.5×IQR（或该范围内的最小值）
    - 下四分位数 Q1：25% 分位
    - 中位数 Q2：箱体内的横线
    - 上四分位数 Q3：75% 分位
    - 上边缘（须）：Q3 + 1.5×IQR（或该范围内的最大值）
    - 须之外的点：异常值（outliers），用单独的点标记

本示例要点：
1. boxplot() 接受“列表的列表”或多组数组
2. patch_artist=True 后才能给箱体填充颜色（否则只能改线条颜色）
3. showmeans=True 同时显示均值（菱形），可与中位数对比看偏态
4. 用 labels（新版 matplotlib 为 tick_labels）设置组名
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 构造四组数据 ----------
rng = np.random.default_rng(2024)

group_a = rng.normal(72, 8, 200)          # 普通班
group_b = rng.normal(78, 10, 200)         # 实验班：均值更高、波动更大
group_c = rng.normal(70, 5, 200)          # 稳定班：波动小
group_d = np.concatenate([rng.normal(66, 6, 190), [98, 99, 15]])  # 含异常值

data = [group_a, group_b, group_c, group_d]
labels = ["一班", "二班", "三班", "四班"]

fig, ax = plt.subplots(figsize=(9, 5.5))

# ---------- 2. 绘制箱线图 ----------
bp = ax.boxplot(
    data,
    tick_labels=labels,       # matplotlib >= 3.9 用 tick_labels；更早版本写 labels
    patch_artist=True,        # 允许填充颜色
    widths=0.5,
    notch=False,              # 凹槽箱体（置信区间）此处不需要
    showmeans=True,           # 显示均值
    meanprops=dict(marker="D", markerfacecolor="#d62728",
                   markeredgecolor="#d62728", markersize=6),
    medianprops=dict(color="#333333", linewidth=2),
    flierprops=dict(marker="o", markerfacecolor="#d62728",
                    markeredgecolor="#d62728", markersize=5, alpha=0.6),
)

# ---------- 3. 逐组设置箱体颜色 ----------
box_colors = ["#a8c8e8", "#f4b183", "#a9d18e", "#d9d2e9"]
for patch, color in zip(bp["boxes"], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.85)

# ---------- 4. 完善图表元素 ----------
ax.set_title("四个班级期末数学成绩分布对比", fontsize=15, fontweight="bold")
ax.set_xlabel("班级", fontsize=11)
ax.set_ylabel("成绩（分）", fontsize=11)
ax.set_ylim(5, 105)
ax.grid(axis="y", linestyle=":", alpha=0.5)
ax.set_axisbelow(True)

# 自定义图例：说明菱形代表均值
from matplotlib.lines import Line2D
legend_items = [
    Line2D([0], [0], color="#333333", lw=2, label="中位数"),
    Line2D([0], [0], marker="D", color="w", markerfacecolor="#d62728",
           markersize=7, label="均值"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#d62728",
           markersize=6, alpha=0.6, label="异常值"),
]
ax.legend(handles=legend_items, loc="lower right", fontsize=9.5)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ---------- 5. 打印五数概括，便于与图形对照 ----------
for name, arr in zip(labels, data):
    q1, q2, q3 = np.percentile(arr, [25, 50, 75])
    iqr = q3 - q1
    print(f"{name}: Q1={q1:.1f}, 中位数={q2:.1f}, Q3={q3:.1f}, "
          f"IQR={iqr:.1f}, 均值={arr.mean():.1f}")

fig.tight_layout()
fig.savefig(BASE / "箱线图示例.png", dpi=150)
plt.show()
