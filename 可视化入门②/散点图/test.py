"""
散点图 · 练习题
=================================
题目背景：
    某连锁咖啡店记录了 30 家门店的“日客流量（人）”与“日营业额（千元）”。

任务要求：
    1. 绘制散点图，点大小 70，颜色用深蓝 "#1f4e79"，透明度 0.7，白色描边。
    2. 用 np.polyfit 拟合一条一次趋势线，用灰色虚线绘制，并在图例中写出方程。
    3. 计算两变量的皮尔逊相关系数 r，用 ax.text() 显示在左上角（保留 2 位小数）。
    4. 找出“日营业额”最高的门店，用 annotate() 标注为“营业额最高 XX 千元”。
    5. 标题“门店客流量与日营业额关系”，x 轴“日客流量（人）”，y 轴“日营业额（千元）”。
    6. 加网格、图例，隐藏上/右边框，保存为 散点图练习.png（dpi=150）。

思考题（写在注释里即可）：
    - 相关系数 r 接近 1 说明什么？能否据此断定“客流量增加导致营业额增加”？
    - 如果散点呈现明显的弯曲形状，用一次趋势线合适吗？

提示：
    - 拟合：k, b = np.polyfit(x, y, 1)
    - 相关：r = np.corrcoef(x, y)[0, 1]
    - 画线：ax.plot([x1, x2], [y1, y2], ...)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

rng = np.random.default_rng(7)
traffic = rng.integers(120, 620, 30).astype(float)
revenue = 3.2 + 0.034 * traffic + rng.normal(0, 3.0, 30)   # 弱到中等正相关
revenue = revenue.clip(2, 30)

fig, ax = plt.subplots(figsize=(8.5, 5.5))

# ============ TODO 1：绘制散点 ============
pass

# ============ TODO 2：拟合趋势线并加入图例 ============
pass

# ============ TODO 3：计算并显示相关系数 ============
pass

# ============ TODO 4：标注营业额最高的门店 ============
pass

# ============ TODO 5 & 6：标题、轴标签、网格、图例、保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# ax.scatter(traffic, revenue, s=70, color="#1f4e79", alpha=0.7,
#            edgecolors="white", linewidths=0.8, label="门店")
#
# k, b = np.polyfit(traffic, revenue, 1)
# xs = np.linspace(traffic.min(), traffic.max(), 50)
# ax.plot(xs, k * xs + b, color="gray", linestyle="--", linewidth=1.8,
#         label=f"趋势线：y = {k:.3f}x + {b:.2f}")
#
# r = np.corrcoef(traffic, revenue)[0, 1]
# ax.text(0.03, 0.95, f"r = {r:.2f}", transform=ax.transAxes,
#         fontsize=11, va="top",
#         bbox=dict(boxstyle="round", fc="white", ec="#cccccc"))
#
# idx = int(np.argmax(revenue))
# ax.annotate(f"营业额最高 {revenue[idx]:.1f} 千元",
#             xy=(traffic[idx], revenue[idx]),
#             xytext=(traffic[idx] - 220, revenue[idx] + 1.5),
#             arrowprops=dict(arrowstyle="->", color="#d62728"),
#             color="#d62728", fontsize=10)
#
# ax.set_title("门店客流量与日营业额关系", fontsize=15, fontweight="bold")
# ax.set_xlabel("日客流量（人）")
# ax.set_ylabel("日营业额（千元）")
# ax.grid(True, linestyle=":", alpha=0.5)
# ax.legend(loc="lower right")
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
#
# fig.tight_layout()
# fig.savefig(BASE / "散点图练习.png", dpi=150)
# plt.show()
