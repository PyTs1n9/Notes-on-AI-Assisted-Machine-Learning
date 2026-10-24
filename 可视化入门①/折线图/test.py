"""
折线图 · 练习
题目：某同学记录了 5 天的学习时长（小时），画出折线图。

要求：
    1. 用 plt.plot 画出 天数 → 学习时长 的折线
    2. 标题写“每天学习时长”，x 轴写“第几天”，y 轴写“小时”
    3. 打开网格
    （保存和显示的代码已经写好了，不用动）

写完后运行：python test.py，看是否生成 折线图练习.png
答案在文件最后，先自己写，再对照。
"""

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 数据（已给出，不用改）
days = [1, 2, 3, 4, 5]
hours = [1.5, 2.0, 1.0, 3.0, 2.5]

# TODO 1：画折线
plt.plot(days, hours, marker="o")

# TODO 2：加标题和坐标轴（plt.title / plt.xlabel / plt.ylabel）
plt.title("每天学习时长")
plt.xlabel("第几天")
plt.ylabel("小时")

# TODO 3：打开网格（plt.grid）
plt.grid()

plt.savefig("折线图练习.png")
plt.show()

# ==================== 参考答案 ====================
# plt.plot(days, hours)
# plt.title("每天学习时长")
# plt.xlabel("第几天")
# plt.ylabel("小时")
# plt.grid()
