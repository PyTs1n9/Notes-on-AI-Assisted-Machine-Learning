## Wine Quality 中 Linear、Ridge、Lasso 对比

**数据集：UCI Wine Quality**

白葡萄酒数据有 4,898 个样本，11 个理化特征，目标 `quality` 为品质评分。:chatgpt-content-reference{index="6"}

[UCI Wine Quality 数据集](https://archive.ics.uci.edu/dataset/186/wine+quality?utm_source=chatgpt.com)

### 训练任务

使用：

```text
winequality-white.csv
```

1. 读取数据并查看字段。
2. 注意该文件默认分隔符是 `;`。
3. 使用 11 个理化指标作为 X。
4. 使用 `quality` 作为 y。
5. 80/20 划分。
6. 使用 `StandardScaler` 对 X 标准化。
7. 分别训练：
   - LinearRegression
   - Ridge(alpha=1.0)
   - Lasso(alpha=0.1)
8. 分别计算：
   - MAE
   - RMSE
   - R²
9. 保存：

```text
output/model_metrics.csv
```

10. 提取三个模型的 `coef_`。
11. 制作特征系数比较表。
12. 绘制系数柱状图。
13. Ridge 分别测试：

```text
alpha = 0.01
0.1
1
10
100
```

14. Lasso 也测试上述 alpha。
15. 记录每个 alpha 对应的 RMSE 和 R²。
16. 绘制 `alpha-RMSE` 曲线。
17. 统计 Lasso 中有多少个系数接近或等于 0。

### 综合分析

回答：

- Linear、Ridge、Lasso 的测试结果是否明显不同？
- alpha 太大后会发生什么？
- 哪些葡萄酒特征对 quality 影响较明显？
- Lasso 为什么可能把某些系数压缩为 0？