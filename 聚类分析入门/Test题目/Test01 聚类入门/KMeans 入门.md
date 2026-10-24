## Wholesale Customers 与 KMeans 入门

**数据集：UCI Wholesale Customers**

该数据集记录批发商客户在 Fresh、Milk、Grocery、Frozen、Detergents_Paper、Delicassen 等商品类别上的年度消费。:chatgpt-content-reference{index="10"}

[UCI Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers?utm_source=chatgpt.com)

### 训练任务

1. 读取数据。
2. 输出字段信息。
3. 今天聚类只使用：

```text
Fresh
Milk
Grocery
Frozen
Detergents_Paper
Delicassen
```

4. 不使用 `Channel` 和 `Region` 训练。
5. 查看 6 个字段的：
   - min
   - max
   - mean
   - std
6. 思考不同量纲是否会影响距离。
7. 使用 StandardScaler。
8. 输出标准化后前 10 行。
9. K=3 完成 KMeans。
10. 给原始数据增加 `cluster`。
11. 统计每个 cluster 有多少客户。
12. 查看 `cluster_centers_`。
13. 将聚类中心还原回原始尺度。
14. 绘制 Fresh—Milk 散点图。
15. 比较未标准化与标准化后的聚类结果。