# matplotlib 可视化入门（基础版）

只讲“能画出图”的最小必要内容：**数据 → 画图 → 标题和坐标轴 → 保存并显示**。
每种图一个文件夹，里面两个文件：`example.py`（照着看）和 `test.py`（照着练）。

## 目录

```
可视化入门①/
├── 折线图/        example.py  test.py
├── 柱状图/
├── 横向柱状图/
├── 散点图/
├── 饼图/
├── 直方图/
├── 箱线图/
├── 热力图/
└── README.md
```

## 怎么运行

进入某个文件夹，再运行脚本：

```bash
cd 折线图
python example.py
```

运行后会在当前文件夹生成一张 png 图片，同时弹出图片窗口。

## 八种图一览

| 图 | 用来回答 | 关键函数 | 一句话记忆 |
|---|---|---|---|
| 折线图 | 怎么变化的 | `plt.plot(x, y)` | 连点成线，看趋势 |
| 柱状图 | 谁多谁少 | `plt.bar(x, y)` | 竖着比大小 |
| 横向柱状图 | 谁多谁少（名字长） | `plt.barh(x, y)` | 把柱子横过来 |
| 散点图 | 两者有没有关系 | `plt.scatter(x, y)` | 一个点是一条数据 |
| 饼图 | 各占多少比例 | `plt.pie(数据, labels=)` | 看部分占整体 |
| 直方图 | 数值怎么分布 | `plt.hist(数据, bins=)` | 数每个区间里有几个 |
| 箱线图 | 几组数据怎么分布 | `plt.boxplot(数据)` | 一个箱子看五数 |
| 热力图 | 表格里哪里强 | `plt.imshow(二维数据)` | 颜色越亮数越大 |

## 通用模板

八种图都是同一个套路，只换中间那一句画图函数：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]   # 中文正常显示
plt.rcParams["axes.unicode_minus"] = False              # 负号正常显示

# 1. 数据
x = ["周一", "周二", "周三"]
y = [18, 20, 17]

# 2. 画图（只改这一句）
plt.plot(x, y)

# 3. 标题和坐标轴
plt.title("标题")
plt.xlabel("横轴名字")
plt.ylabel("纵轴名字")

# 4. 保存并显示
plt.savefig("图片名.png")
plt.show()
```

## 三个小提醒

1. **x 和 y 的个数必须一样**，否则报错。
2. **`savefig` 要写在 `show` 前面**，顺序反了会存成空白图。
3. **中文显示成方块**时，检查有没有写 `font.sans-serif` 那两行配置（Windows 用 `"Microsoft YaHei"`，macOS 用 `"PingFang SC"`）。

## 练习怎么用

`test.py` 里数据已经给好了，你只需要补上被 `TODO` 标出的几行。文件最后有参考答案，**先自己写，写完再对照**。
