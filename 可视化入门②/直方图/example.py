"""
直方图（Histogram）示例
=================================
适用场景：
    展示单个连续变量的“分布形态”——集中趋势、偏度、双峰、离群值。

直方图 vs 柱状图（最容易被混淆的一对）：
    | 对比项   | 柱状图              | 直方图                      |
    |----------|---------------------|-----------------------------|
    | x 轴含义 | 离散类别            | 连续区间的分箱（bins）      |
    | 柱间间隙 | 有间隙（表示不同类别）| 无间隙（区间首尾相接）      |
    | 关注点   | 各类别数值大小比较  | 数据在各区间的分布密度      |

本示例要点：
1. hist() 的 bins 控制分箱数量，数量过少会掩盖细节，过多会呈锯齿状
2. density=True 时纵轴为概率密度，所有柱面积之和为 1
3. 叠加均值线、中位数线，可直观看出分布的偏移
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 生成数据：1000 名学生的高考数学成绩 ----------
rng = np.random.default_rng(2025)
scores = rng.normal(loc=68, scale=13, size=1000).clip(20, 100)

fig, ax = plt.subplots(figsize=(9, 5))

# ---------- 2. 绘制直方图 ----------
counts, bins, patches = ax.hist(
    scores,
    bins=20,                  # 分 20 个区间
    color="#5b8ff9",
    edgecolor="white",        # 白色描边，区分相邻柱子
    linewidth=1.0,
    alpha=0.85,
    density=False,            # 纵轴用“人数”（频数）
    label="成绩分布",
)

# ---------- 3. 叠加均值线与中位数线 ----------
mean_val = scores.mean()
median_val = np.median(scores)

ax.axvline(mean_val, color="#d62728", linestyle="--", linewidth=1.8,
           label=f"均值 = {mean_val:.1f}")
ax.axvline(median_val, color="#2a9d8f", linestyle=":", linewidth=1.8,
           label=f"中位数 = {median_val:.1f}")

# ---------- 4. 在右上角补充统计信息 ----------
stats_text = (
    f"样本量 n = {len(scores)}\n"
    f"标准差 = {scores.std():.1f}\n"
    f"最小值 = {scores.min():.0f}    最大值 = {scores.max():.0f}"
)
ax.text(0.02, 0.96, stats_text, transform=ax.transAxes,
        va="top", fontsize=10, family="Microsoft YaHei",
        bbox=dict(boxstyle="round,pad=0.5", fc="#f7f7f7", ec="#cccccc"))

# ---------- 5. 完善图表元素 ----------
ax.set_title("1000名学生数学成绩分布直方图", fontsize=15, fontweight="bold")
ax.set_xlabel("成绩（分）", fontsize=11)
ax.set_ylabel("人数", fontsize=11)
ax.grid(axis="y", linestyle=":", alpha=0.5)
ax.set_axisbelow(True)
ax.legend(loc="upper right", fontsize=10)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(BASE / "直方图示例.png", dpi=150)
plt.show()
