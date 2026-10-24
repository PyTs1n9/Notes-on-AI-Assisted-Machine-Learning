"""
饼图 · 练习题
=================================
题目背景：
    某App用户来源渠道分布（百分比）。

任务要求：
    1. 绘制饼图，数据为 sources / ratios。
    2. 把占比最高的渠道用 explode 抽出 0.1 的距离。
    3. 显示百分比（保留 1 位小数），百分比文字为白色加粗。
    4. 从 12 点方向开始顺时针绘制（startangle=90, counterclock=False）。
    5. 扇区之间用白色描边分隔，线宽 2。
    6. 标题“App 用户来源渠道分布”，保证饼图为正圆（axis("equal")）。
    7. 保存为 饼图练习.png（dpi=150）。

思考题（写在注释里）：
    - 5 个渠道中“应用商店 + 搜索”合计占多少？饼图能一眼看出“合计”吗？
    - 如果渠道增加到 12 个，应该换成什么图更合适？为什么？

提示：
    - explode 需要与数据等长的列表，例如 [0.1, 0, 0, 0, 0]
    - 若要让“最大项”自动突出：idx = int(np.argmax(ratios))
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

sources = ["应用商店", "搜索引擎", "社交分享", "广告投放", "其他"]
ratios = np.array([38.0, 25.5, 18.0, 12.5, 6.0])

fig, ax = plt.subplots(figsize=(7.5, 6.5))

# ============ TODO 1 & 2：准备 explode 并绘制饼图 ============
pass

# ============ TODO 3：百分比文字样式（白色加粗） ============
pass

# ============ TODO 4 ~ 6：方向、描边、标题、正圆 ============
pass

# ============ TODO 7：保存 ============
pass

# ============================================================================
# 参考答案
# ============================================================================
# idx = int(np.argmax(ratios))
# explode = [0.1 if i == idx else 0 for i in range(len(ratios))]
#
# wedges, texts, autotexts = ax.pie(
#     ratios, labels=sources, explode=explode,
#     autopct="%1.1f%%", startangle=90, counterclock=False,
#     pctdistance=0.68, textprops={"fontsize": 11},
#     wedgeprops={"edgecolor": "white", "linewidth": 2},
# )
#
# for t in autotexts:
#     t.set_color("white")
#     t.set_fontweight("bold")
#
# ax.set_title("App 用户来源渠道分布", fontsize=15, fontweight="bold", pad=18)
# ax.axis("equal")
#
# fig.tight_layout()
# fig.savefig(BASE / "饼图练习.png", dpi=150)
# plt.show()
