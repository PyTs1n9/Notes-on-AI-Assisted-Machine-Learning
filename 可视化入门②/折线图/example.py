"""
折线图（Line Chart）示例
=================================
适用场景：展示数据随时间（或有序类别）变化的趋势，强调“走势”而非“比较大小”。

本示例要点：
1. plot() 绘制折线，x/y 长度必须一致
2. 通过 color / linestyle / linewidth / marker 区分多条曲线
3. 图例 legend()、网格 grid()、坐标轴标签、标题
4. annotate() 标注极值点，突出关键信息
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

# ---------- 0. 中文显示配置（Windows 常用微软雅黑，缺失时回退黑体） ----------
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

# ---------- 1. 准备数据 ----------
months = ["1月", "2月", "3月", "4月", "5月", "6月",
          "7月", "8月", "9月", "10月", "11月", "12月"]

# 两家门店的月销售额（单位：万元）
store_a = np.array([32, 28, 41, 55, 62, 71, 78, 83, 69, 58, 63, 92])
store_b = np.array([25, 26, 33, 40, 47, 52, 60, 61, 55, 49, 52, 70])

# ---------- 2. 创建画布 ----------
fig, ax = plt.subplots(figsize=(9, 5))  # figsize 单位是英寸

# ---------- 3. 绘制两条折线 ----------
# 门店 A：实线 + 圆点标记，标记处带橙色填充
ax.plot(months, store_a,
        color="#d62728",          # 线条颜色：中国习惯用红色表示“好/增长”
        linestyle="-",            # 线条样式：实线
        linewidth=2.2,
        marker="o",               # 数据点标记：圆形
        markersize=6,
        markerfacecolor="white",  # 标记内部填充白色
        markeredgecolor="#d62728",
        label="门店A")

# 门店 B：虚线 + 三角标记
ax.plot(months, store_b,
        color="#1f77b4",
        linestyle="--",
        linewidth=2.0,
        marker="^",
        markersize=6,
        label="门店B")

# ---------- 4. 标注门店 A 的最高点 ----------
peak_idx = int(np.argmax(store_a))
ax.annotate(
    f"全年最高 {store_a[peak_idx]} 万",
    xy=(peak_idx, store_a[peak_idx]),          # 箭头指向的点
    xytext=(peak_idx - 3.2, store_a[peak_idx] + 4),  # 文字位置
    fontsize=10,
    color="#d62728",
    arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.2),
)

# ---------- 5. 完善图表元素 ----------
ax.set_title("2025年两家门店月度销售额走势", fontsize=15, fontweight="bold", pad=12)
ax.set_xlabel("月份", fontsize=11)
ax.set_ylabel("销售额（万元）", fontsize=11)
ax.set_ylim(0, 105)              # 纵轴从 0 开始，避免夸大差异
ax.grid(True, linestyle=":", alpha=0.6)   # 网格线：点线 + 半透明
ax.legend(loc="upper left", frameon=True, fontsize=10)  # 图例位置

# 隐藏上方和右侧的边框，视觉更干净（可选）
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ---------- 6. 保存与展示 ----------
fig.tight_layout()               # 自动调整布局，防止标签被裁掉
fig.savefig(BASE / "折线图示例.png", dpi=150)
plt.show()
