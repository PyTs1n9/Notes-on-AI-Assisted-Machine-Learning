"""
散点图（Scatter Plot）示例
=================================
适用场景：
    观察两个连续变量之间的关系（正相关 / 负相关 / 无关）、发现离群点、
    按第三个变量做颜色或大小编码。

本示例要点：
1. scatter() 的 x、y 是等长的数值数组
2. s 控制点面积，c 可以用数值数组做颜色映射，配合 colorbar 解释颜色含义
3. alpha 设置透明度，解决点重叠（overplotting）问题
4. 可以叠加一条趋势线（一元线性拟合）辅助判断相关性
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 构造数据 ----------
rng = np.random.default_rng(42)      # 固定随机种子，保证每次结果一致
n = 120

study_hours = rng.normal(4.5, 1.6, n).clip(0.5, 9)          # 每周学习时长
# 成绩与学习时长正相关，再叠加噪声
score = 45 + 6.2 * study_hours + rng.normal(0, 7, n)
score = score.clip(20, 100)

# 第三个维度：出勤率（用于颜色编码）
attendance = rng.uniform(60, 100, n)

fig, ax = plt.subplots(figsize=(8.5, 5.5))

# ---------- 2. 绘制散点 ----------
sc = ax.scatter(study_hours, score,
                s=55,                    # 点的大小
                c=attendance,            # 用出勤率做颜色映射
                cmap="RdYlGn",           # 颜色条：红-黄-绿
                alpha=0.75,              # 透明度，缓解重叠
                edgecolors="white",      # 白色描边让点更清晰
                linewidths=0.8)

# ---------- 3. 添加颜色条 ----------
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label("出勤率（%）", fontsize=10)

# ---------- 4. 叠加一元线性拟合趋势线 ----------
k, b = np.polyfit(study_hours, score, 1)          # 一次多项式拟合：y = kx + b
xs = np.linspace(study_hours.min(), study_hours.max(), 50)
ax.plot(xs, k * xs + b,
        color="#333333", linestyle="--", linewidth=1.8,
        label=f"拟合趋势：y = {k:.1f}x + {b:.0f}")

# 计算皮尔逊相关系数
r = np.corrcoef(study_hours, score)[0, 1]
ax.text(0.03, 0.95, f"相关系数 r = {r:.2f}",
        transform=ax.transAxes, fontsize=11,
        va="top", bbox=dict(boxstyle="round", fc="white", ec="#cccccc"))

# ---------- 5. 完善图表元素 ----------
ax.set_title("每周学习时长与考试成绩的关系", fontsize=15, fontweight="bold")
ax.set_xlabel("每周学习时长（小时）", fontsize=11)
ax.set_ylabel("考试成绩（分）", fontsize=11)
ax.grid(True, linestyle=":", alpha=0.5)
ax.legend(loc="lower right", fontsize=9.5)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(BASE / "散点图示例.png", dpi=150, bbox_inches="tight")
plt.show()
