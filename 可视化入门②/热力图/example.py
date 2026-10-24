"""
热力图（Heatmap）示例
=================================
适用场景：
    用“颜色深浅”表达二维矩阵中的数值大小，适合：
    1. 相关系数矩阵（特征之间谁和谁相关）
    2. 交叉表（如 星期 × 小时 的客流强度）
    3. 混淆矩阵、地理网格数据

本示例要点：
1. imshow() 把二维数组渲染成色块；origin="upper" 让第 0 行显示在顶部
2. cmap 选择色阶：相关系数用 "RdBu_r"（蓝-白-红双向），单向量用 "YlOrRd"
3. vmin / vmax 固定色标范围，本例设为 -1 / 1，保证 0 值正好落在白色
4. 用双层循环 + ax.text() 在每个格子写入数值
5. 用 mask 隐藏上三角（矩阵对称时避免信息重复）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent   # 脚本所在目录：保证图片总保存在本文件夹内

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 模拟 6 个变量的数据 ----------
rng = np.random.default_rng(88)
n = 300

study = rng.normal(4, 1.2, n)                  # 学习时长
attendance = 70 + 4 * study + rng.normal(0, 6, n)   # 出勤率
homework = 50 + 6 * study + rng.normal(0, 8, n)     # 作业完成度
sleep = rng.normal(7, 1.1, n)                  # 睡眠时长
midterm = 40 + 5 * study + 0.25 * homework + 0.1 * attendance + rng.normal(0, 6, n)
final = 0.6 * midterm + 3 * study + rng.normal(0, 7, n)

features = ["学习时长", "出勤率", "作业完成度", "睡眠时长", "期中成绩", "期末成绩"]
matrix = np.vstack([study, attendance, homework, sleep, midterm, final])

# ---------- 2. 计算皮尔逊相关系数矩阵 ----------
corr = np.corrcoef(matrix)     # 形状 6×6，取值 [-1, 1]，对角线为 1

# ---------- 3. 生成上三角遮罩（可选） ----------
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)   # 只遮住严格上三角
corr_masked = np.ma.masked_where(mask, corr)

fig, ax = plt.subplots(figsize=(8, 6.5))

# ---------- 4. 绘制热力图 ----------
im = ax.imshow(corr_masked,
               cmap="RdBu_r",     # 红蓝双向色阶：红=正相关，蓝=负相关
               vmin=-1, vmax=1,   # 固定色标范围
               origin="upper",
               interpolation="nearest")

# ---------- 5. 在每个格子写入数值 ----------
for i in range(len(features)):
    for j in range(len(features)):
        if mask[i, j]:             # 被遮罩的格子不写字
            continue
        value = corr[i, j]
        # 深色背景用白字，浅色背景用黑字，保证可读性
        color = "white" if abs(value) > 0.6 else "#222222"
        ax.text(j, i, f"{value:.2f}",
                ha="center", va="center", fontsize=10,
                color=color, fontweight="bold" if i == j else "normal")

# ---------- 6. 坐标轴刻度 ----------
ax.set_xticks(np.arange(len(features)))
ax.set_yticks(np.arange(len(features)))
ax.set_xticklabels(features, rotation=35, ha="right", fontsize=10)
ax.set_yticklabels(features, fontsize=10)

# 让刻度线落在格子中心之外，视觉更整齐（可选）
ax.set_xticks(np.arange(-0.5, len(features), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(features), 1), minor=True)
ax.grid(which="minor", color="white", linestyle="-", linewidth=2)
ax.tick_params(which="minor", length=0)   # 隐藏次要刻度的小短线

# ---------- 7. 颜色条 ----------
cbar = fig.colorbar(im, ax=ax, shrink=0.82, pad=0.03)
cbar.set_label("皮尔逊相关系数 r", fontsize=10)
cbar.ax.tick_params(labelsize=9)

ax.set_title("学生成绩影响因素 · 相关系数热力图", fontsize=15,
             fontweight="bold", pad=14)

fig.tight_layout()
fig.savefig(BASE / "热力图示例.png", dpi=150)
plt.show()
