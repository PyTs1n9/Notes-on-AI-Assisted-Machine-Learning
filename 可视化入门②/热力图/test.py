"""
热力图 · 练习题
=================================
题目背景：
    一家便利店统计了“工作日 × 时段”的平均客流（人/小时），
    数据是一个 7×6 的二维矩阵：7 天（周一~周日） × 6 个时段。

任务要求：
    1. 用 imshow() 绘制热力图，色阶使用 "YlOrRd"，origin="upper"。
    2. 每个格子内写入客流数值（整数），并保证数字在任何背景色下都清晰可读
       （提示：数值大于阈值时用白色字，否则用深色字）。
    3. x 轴显示 6 个时段，y 轴显示 7 天，x 轴标签文字旋转 30° 且右对齐。
    4. 添加颜色条，标签为“平均客流（人/小时）”，并缩小到 0.85。
    5. 标题“便利店工作日 × 时段客流热力图”，加白色网格线分隔格子。
    6. 用 annotate 或 text 标出全图客流最高的格子（可以只打印到控制台）。
    7. 保存为 热力图练习.png（dpi=150）。

思考题（写在注释里）：
    - 客流高峰出现在哪两个时段的组合？对排班有什么建议？
    - 热力图和散点图都能表达两个维度，什么时候优先用热力图？
    - 如果矩阵是 30×48（30 天 × 每半小时），格子里的数字还该不该写？为什么？

提示：
    - 网格线：ax.set_xticks(np.arange(-0.5, cols, 1), minor=True) 再 ax.grid(which="minor", ...)
    - 最大值位置：idx = np.unravel_index(np.argmax(grid), grid.shape)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
slots = ["6-9点", "9-12点", "12-15点", "15-18点", "18-21点", "21-24点"]

grid = np.array([
    [18, 25, 42, 30, 55, 28],   # 周一
    [16, 23, 40, 29, 52, 26],   # 周二
    [17, 24, 41, 31, 54, 27],   # 周三
    [19, 26, 43, 33, 58, 30],   # 周四
    [21, 28, 46, 36, 66, 38],   # 周五
    [25, 48, 62, 55, 78, 60],   # 周六
    [24, 46, 60, 52, 72, 55],   # 周日
], dtype=float)

fig, ax = plt.subplots(figsize=(8.5, 6))

# ============ TODO 1：绘制热力图 ============
pass

# ============ TODO 2：格子内写数值（自适应字体颜色） ============
pass

# ============ TODO 3：坐标轴刻度与标签 ============
pass

# ============ TODO 4：颜色条 ============
pass

# ============ TODO 5 & 6：标题、网格线、最大值标注 ============
pass

# ============ TODO 7：保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# im = ax.imshow(grid, cmap="YlOrRd", origin="upper", aspect="auto")
#
# thr = grid.max() * 0.6
# for i in range(grid.shape[0]):
#     for j in range(grid.shape[1]):
#         v = grid[i, j]
#         ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=10,
#                 color="white" if v > thr else "#333333")
#
# ax.set_xticks(np.arange(len(slots)))
# ax.set_yticks(np.arange(len(days)))
# ax.set_xticklabels(slots, rotation=30, ha="right")
# ax.set_yticklabels(days)
#
# ax.set_xticks(np.arange(-0.5, len(slots), 1), minor=True)
# ax.set_yticks(np.arange(-0.5, len(days), 1), minor=True)
# ax.grid(which="minor", color="white", linestyle="-", linewidth=1.5)
# ax.tick_params(which="minor", length=0)
#
# cbar = fig.colorbar(im, ax=ax, shrink=0.85)
# cbar.set_label("平均客流（人/小时）")
#
# ax.set_title("便利店工作日 × 时段客流热力图", fontsize=15,
#              fontweight="bold", pad=14)
#
# idx = np.unravel_index(np.argmax(grid), grid.shape)
# print(f"客流最高：{days[idx[0]]} {slots[idx[1]]} = {grid[idx]} 人/小时")
#
# fig.tight_layout()
# fig.savefig(BASE / "热力图练习.png", dpi=150)
# plt.show()
