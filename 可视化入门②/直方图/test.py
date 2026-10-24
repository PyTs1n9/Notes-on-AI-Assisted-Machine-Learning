"""
直方图 · 练习题
=================================
题目背景：
    某客服系统记录了 800 次通话的“通话时长（秒）”。
    这类数据通常右偏（少数长通话把分布拉出长尾）。

任务要求：
    1. bins 设为 30，绘制直方图，颜色 "#7b9e89"，白色描边，透明度 0.85。
    2. 用 axvline 画出均值线（红色虚线）和中位数线（橙色点线），并在图例中标注数值。
    3. 观察均值与中位数的位置关系，在控制台 print 一句结论（右偏/左偏/近似对称）。
    4. 标题“客服通话时长分布（n=800）”，x 轴“通话时长（秒）”，y 轴“通话次数”。
    5. 加横向网格、图例（右上角），隐藏上/右边框。
    6. 保存为 直方图练习.png（dpi=150）。

进阶（可选）：
    - 追加 density=True 再画一条 KDE 曲线（可用 scipy.stats.gaussian_kde）；
    - 用 ax.set_xlim(0, 600) 截断长尾，观察图形变化；
    - 把 bins 改成 5、50，观察“分箱数”对形态解读的影响。

判断偏度的经验法则：
    均值 > 中位数 → 右偏（长尾在右）；均值 < 中位数 → 左偏（长尾在左）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# 通话时长：对数正态分布，天然右偏
rng = np.random.default_rng(11)
durations = rng.lognormal(mean=4.3, sigma=0.75, size=800).clip(5, 600)

fig, ax = plt.subplots(figsize=(9, 5))

# ============ TODO 1：绘制直方图 ============
pass

# ============ TODO 2：均值线与中位数线 ============
pass

# ============ TODO 3：打印偏度结论 ============
pass

# ============ TODO 4 & 5：标题、轴标签、网格、图例、边框 ============
pass

# ============ TODO 6：保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# ax.hist(durations, bins=30, color="#7b9e89", edgecolor="white",
#         linewidth=0.8, alpha=0.85, label="通话时长")
#
# mean_val, median_val = durations.mean(), np.median(durations)
# ax.axvline(mean_val, color="#d62728", linestyle="--", linewidth=1.8,
#            label=f"均值 = {mean_val:.1f}s")
# ax.axvline(median_val, color="#ff7f0e", linestyle=":", linewidth=1.8,
#            label=f"中位数 = {median_val:.1f}s")
#
# if mean_val > median_val:
#     print("均值 > 中位数 → 分布右偏（长尾在右侧）")
# elif mean_val < median_val:
#     print("均值 < 中位数 → 分布左偏（长尾在左侧）")
# else:
#     print("均值 ≈ 中位数 → 分布近似对称")
#
# ax.set_title(f"客服通话时长分布（n={len(durations)}）", fontsize=15, fontweight="bold")
# ax.set_xlabel("通话时长（秒）")
# ax.set_ylabel("通话次数")
# ax.grid(axis="y", linestyle=":", alpha=0.5)
# ax.set_axisbelow(True)
# ax.legend(loc="upper right")
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
#
# fig.tight_layout()
# fig.savefig(BASE / "直方图练习.png", dpi=150)
# plt.show()
