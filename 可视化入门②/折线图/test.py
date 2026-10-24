"""
折线图 · 练习题
=================================
题目背景：
    某产品上线后，记录了 8 周的“访问量”与“下单量”（单位：次）。

任务要求（共 6 项，逐个完成）：
    1. 在同一张图上绘制两条折线：访问量用蓝色实线 + 圆点，下单量用橙色虚线 + 方块标记。
    2. 给两条折线加上图例，位置放在右上角。
    3. 标题设为“产品上线后 8 周流量与转化趋势”，x 轴标签“周次”，y 轴标签“次数”。
    4. 打开网格线（虚线、半透明），并隐藏上方和右侧的边框。
    5. 用 annotate() 标出“访问量”最高的一周，文字内容为“峰值 XXX”。
    6. 保存为 折线图练习.png（dpi=150），并调用 plt.show() 显示。

评分要点：
    - 两条线颜色/线型/标记各不相同，图例能正确对应
    - 纵轴从 0 开始
    - 标注的箭头指向正确的数据点

提示：把下方 TODO 处的 pass 替换为你的代码，运行 `python test.py` 查看效果。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# 数据（已给出，勿修改）
weeks = [f"第{i}周" for i in range(1, 9)]
visits = np.array([1200, 1580, 2100, 2650, 2480, 3100, 3550, 3420])
orders = np.array([120, 168, 235, 310, 288, 402, 470, 455])

fig, ax = plt.subplots(figsize=(9, 5))

# ============ TODO 1：绘制两条折线 ============
# 提示：ax.plot(x, y, color=..., linestyle=..., marker=..., label=...)
pass

# ============ TODO 2：添加图例（右上角） ============
pass

# ============ TODO 3：设置标题与坐标轴标签 ============
pass

# ============ TODO 4：网格线 + 隐藏上/右边框 ============
pass

# ============ TODO 5：标注访问量最高的一周 ============
# 提示：peak_idx = int(np.argmax(visits))，再用 ax.annotate(...)
pass

# ============ TODO 6：保存并显示 ============
pass

# ============================================================================
# 参考答案（务必先自己写完再看）
# ============================================================================
# ax.plot(weeks, visits, color="#1f77b4", linestyle="-", linewidth=2,
#         marker="o", label="访问量")
# ax.plot(weeks, orders, color="#ff7f0e", linestyle="--", linewidth=2,
#         marker="s", label="下单量")
#
# ax.legend(loc="upper right")
#
# ax.set_title("产品上线后 8 周流量与转化趋势", fontsize=15, fontweight="bold")
# ax.set_xlabel("周次")
# ax.set_ylabel("次数")
# ax.set_ylim(0, max(visits) * 1.15)
#
# ax.grid(True, linestyle=":", alpha=0.6)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
#
# peak_idx = int(np.argmax(visits))
# ax.annotate(f"峰值 {visits[peak_idx]}",
#             xy=(peak_idx, visits[peak_idx]),
#             xytext=(peak_idx - 2.5, visits[peak_idx] + 500),
#             arrowprops=dict(arrowstyle="->", color="gray"))
#
# fig.tight_layout()
# fig.savefig(BASE / "折线图练习.png", dpi=150)
# plt.show()
