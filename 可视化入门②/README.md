# matplotlib 可视化入门：8 种基础图表

面向零基础到进阶的 matplotlib 实操材料。每种图表一个独立文件夹，内含**示例**（带逐行注释）与**练习题**（任务要求 + 待填代码 + 参考答案）。

---

## 1. 目录结构

```
可视化入门/
├── README.md
├── 折线图/          example.py  test.py  折线图示例.png  折线图练习_参考答案.png
├── 柱状图/          example.py  test.py  柱状图示例.png  柱状图练习_参考答案.png
├── 横向柱状图/      example.py  test.py  ...
├── 散点图/          example.py  test.py  ...
├── 饼图/            example.py  test.py  ...
├── 直方图/          example.py  test.py  ...
├── 箱线图/          example.py  test.py  ...
└── 热力图/          example.py  test.py  ...
```

- `example.py`：可运行的完整示例，注释覆盖每个参数的作用，运行后在同目录生成 `xxx示例.png`
- `test.py`：练习题。文件上半部分是**题目要求**，中间是 `TODO` 待填代码，末尾是**参考答案**（整段注释，建议做完再看）
- `xxx练习_参考答案.png`：参考答案的运行效果，用于自查

## 2. 环境要求

```bash
python -c "import matplotlib, numpy; print(matplotlib.__version__, numpy.__version__)"
# 建议 matplotlib >= 3.6，numpy >= 1.22
```

未安装时：`pip install matplotlib numpy`

## 3. 运行方式

```bash
cd 折线图
python example.py
```

脚本内部用 `BASE = Path(__file__).parent` 定位输出目录，因此**从任意路径运行，图片都会保存在脚本所在文件夹**，不会散落到当前工作目录。
若在无图形界面的环境（服务器、IDE 的批处理模式）运行，设置环境变量 `MPLBACKEND=Agg` 即可只保存图片、不弹窗。

## 4. 图表选型速查

| 图表 | 回答什么问题 | 核心函数 | 关键参数 | 典型易错点 |
|---|---|---|---|---|
| 折线图 | 随时间/有序量的**趋势** | `ax.plot()` | `marker` `linestyle` `label` | 多条线不设 `label` 导致无图例；纵轴不从 0 起夸大差异 |
| 柱状图 | 类别之间的**大小比较** | `ax.bar()` | `width` `color` `ax.bar_label()` | 分组柱需错开 x 位置（±width/2）；刻度要对齐类别中心 |
| 横向柱状图 | 类别多、名称长、做**排行榜** | `ax.barh()` | `height` `np.argsort` | 忘记排序；x/y 含义与 `bar` 互换 |
| 散点图 | 两个连续变量的**相关关系**、离群点 | `ax.scatter()` | `s` `c` `alpha` `cmap` | 点重叠严重时不用 `alpha`；用相关系数代替“因果结论” |
| 饼图 | **部分占整体**的比例 | `ax.pie()` | `explode` `autopct` `startangle` | 类别超过 7 个仍用饼图；不加 `axis("equal")` 变成椭圆 |
| 直方图 | 单个变量的**分布形态** | `ax.hist()` | `bins` `density` `edgecolor` | 与柱状图混用；`bins` 过少/过多误读分布 |
| 箱线图 | 多组数据的**分布差异与异常值** | `ax.boxplot()` | `patch_artist` `flierprops` `widths` | 3.9+ 参数改名为 `tick_labels`；箱线图看不出双峰 |
| 热力图 | **二维矩阵**的强弱（相关矩阵、交叉表） | `ax.imshow()` | `cmap` `vmin/vmax` `origin` | 不固定 `vmin/vmax` 导致跨图不可比；深色格子配深色字 |

选型决策（自上而下判断）：

1. 数据是“部分 + 整体”，且类别 ≤ 7 → **饼图**
2. x 轴是时间或有序序列 → **折线图**
3. 两个连续变量看关系 → **散点图**；一个连续变量看分布 → **直方图**；多组分布对比 → **箱线图**
4. 类别比较 → 类别 ≤ 8 用**竖向柱状图**，类别多或名称长用**横向柱状图**
5. 数据是二维矩阵（行/列都有业务含义） → **热力图**

## 5. 通用代码骨架

所有示例都遵循同一结构，建议把它固化成肌肉记忆：

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(9, 5))   # 1. 画布
ax.plot(x, y, label="系列A")              # 2. 绘图（可多次）
ax.set_title("标题", fontsize=15, fontweight="bold")
ax.set_xlabel("X 轴"); ax.set_ylabel("Y 轴")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="best")                     # 3. 装饰
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()                        # 4. 防裁切
fig.savefig(BASE / "输出.png", dpi=150)   # 5. 先保存
plt.show()                                # 6. 再显示
```

## 6. 中文显示

```python
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False   # 修复负号显示为方块
```

Windows 自带微软雅黑；macOS 可用 `"PingFang SC"` / `"Heiti SC"`；Linux 需先安装中文字体（如 `fonts-wqy-zenhei`）再指定字体名。

## 7. 五个高频坑

1. **`labels` 参数已被移除**：`boxplot` 从 3.9 起改用 `tick_labels`，3.11 起写 `labels=` 会直接报 `TypeError`。
2. **`savefig` 必须在 `show` 之前**：`plt.show()` 关闭窗口后 figure 会失效，之后再保存得到空白图。
3. **`fig.tight_layout()` 不是万能**：颜色条、长图例会挤压边缘，必要时用 `bbox_inches="tight"`。
4. **图例遮挡数据**：优先 `loc="best"`，或 `bbox_to_anchor=(1.02, 1)` 把图例移到画布外。
5. **中文字体只对当前进程生效**：每个脚本都要显式设置 `rcParams`，或写进一个公共模块统一导入。

## 8. 建议学习顺序

1. 折线图 → 掌握 `fig/ax` 结构、标签、图例、网格（最基础，其他图都在此骨架上替换绘图函数）
2. 柱状图 → 横向柱状图（同一函数族，注意排序与坐标互换）
3. 散点图 → 理解颜色映射与 `colorbar`
4. 直方图 → 箱线图（一对互补的“分布”工具，配合阅读顺序理解五数概括）
5. 饼图 → 热力图（分别对应“比例”和“矩阵”两种特殊数据结构）

每节的练习建议先独立完成，再对照参考答案与效果图检查：图形元素是否齐全、坐标轴是否合理、是否存在遮挡或误导性缩放。
