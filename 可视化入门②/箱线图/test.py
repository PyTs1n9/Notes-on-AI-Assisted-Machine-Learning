"""
箱线图 · 练习题
=================================
题目背景：
    三家供应商提供的零件尺寸（目标值 50mm），各抽检 100 件。

任务要求：
    1. 绘制箱线图，箱体宽度 0.45，允许填充颜色。
    2. 三个箱体分别填充 "#a8c8e8"、"#f4b183"、"#a9d18e"，透明度 0.85。
    3. 中位数线为深灰色（#333333）线宽 2；异常值用红色圆点（大小 5，透明度 0.6）。
    4. 用 axhline 画一条 y=50 的绿色参考线，标注“目标尺寸 50mm”。
    5. 标题“三家供应商零件尺寸抽检分布”，y 轴“尺寸（mm）”，y 轴范围 44~56。
    6. 控制台打印每家供应商的 Q1、中位数、Q3、IQR 与异常值个数。
    7. 保存为 箱线图练习.png（dpi=150）。

思考题（写在注释里）：
    - 哪家供应商的“稳定性”最好？看哪个指标判断（提示：IQR / 须长）？
    - 某家供应商中位数达标但异常值很多，说明什么？
    - 箱线图能否看出“双峰分布”？不能的话应该用什么图？

提示：
    - 异常值判定：低于 Q1-1.5×IQR 或高于 Q3+1.5×IQR
    - matplotlib 3.9 起，boxplot 的 labels 参数改名为 tick_labels；
      更早版本写 labels=（3.11 起 labels 已彻底移除，会报 TypeError）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

rng = np.random.default_rng(5)
supplier_a = rng.normal(50.0, 0.8, 100)
supplier_b = rng.normal(50.4, 1.6, 100)
supplier_c = np.concatenate([rng.normal(49.8, 0.5, 95), rng.normal(53.5, 0.3, 5)])

data = [supplier_a, supplier_b, supplier_c]
labels = ["供应商A", "供应商B", "供应商C"]

fig, ax = plt.subplots(figsize=(9, 5.5))

# ============ TODO 1 & 2：绘制箱线图并填充颜色 ============
pass

# ============ TODO 3：中位数线、异常值样式 ============
pass

# ============ TODO 4：目标尺寸参考线 ============
pass

# ============ TODO 5 & 7：标题、轴标签、范围、保存 ============
pass

# ============ TODO 6：打印统计量 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# bp = ax.boxplot(
#     data, tick_labels=labels, patch_artist=True, widths=0.45,
#     medianprops=dict(color="#333333", linewidth=2),
#     flierprops=dict(marker="o", markerfacecolor="#d62728",
#                     markeredgecolor="#d62728", markersize=5, alpha=0.6),
# )
# for patch, color in zip(bp["boxes"], ["#a8c8e8", "#f4b183", "#a9d18e"]):
#     patch.set_facecolor(color)
#     patch.set_alpha(0.85)
#
# ax.axhline(50, color="#2a9d8f", linestyle="--", linewidth=1.6,
#            label="目标尺寸 50mm")
# ax.legend(loc="upper left")
#
# ax.set_title("三家供应商零件尺寸抽检分布", fontsize=15, fontweight="bold")
# ax.set_ylabel("尺寸（mm）")
# ax.set_ylim(44, 56)
# ax.grid(axis="y", linestyle=":", alpha=0.5)
# ax.set_axisbelow(True)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
#
# for name, arr in zip(labels, data):
#     q1, q2, q3 = np.percentile(arr, [25, 50, 75])
#     iqr = q3 - q1
#     n_out = int(((arr < q1 - 1.5 * iqr) | (arr > q3 + 1.5 * iqr)).sum())
#     print(f"{name}: Q1={q1:.2f}, 中位数={q2:.2f}, Q3={q3:.2f}, "
#           f"IQR={iqr:.2f}, 异常值={n_out} 个")
#
# fig.tight_layout()
# fig.savefig(BASE / "箱线图练习.png", dpi=150)
# plt.show()
