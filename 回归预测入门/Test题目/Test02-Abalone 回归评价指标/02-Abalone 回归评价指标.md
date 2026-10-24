## 9月25日：Abalone 回归评价指标

**数据集：UCI Abalone**

任务目标是根据鲍鱼物理测量值预测 Rings。UCI 原始数据有 4,177 个样本。:chatgpt-content-reference{index="4"}

[UCI Abalone 数据集](https://archive.ics.uci.edu/dataset/1/abalone?utm_source=chatgpt.com)

### 训练任务

1. 下载数据并读取。
2. 查看所有字段。
3. 今天暂时不使用 `Sex` 字段，只保留数值字段。
4. 使用 `Rings` 作为 y。
5. 80/20 划分训练测试集。
6. 训练线性回归。
7. 计算：
   - MAE
   - MSE
   - RMSE
   - R²
8. 将四个指标保存到：

```text
output/metrics.csv
```

9. 手工选出 5 个样本，根据真实值和预测值计算绝对误差。
10. 检查手工计算的 MAE 与 Python 计算是否一致。
11. 从测试结果中找：
    - 预测最准确的 10 条；
    - 预测误差最大的 10 条。
12. 分析这些样本是否存在共同特点。
13. 绘制：
    - 真实值—预测值散点图；
    - 残差图；
    - 绝对误差直方图。
14. 人为把 5 条预测结果增加 20。
15. 再次计算 MAE 和 RMSE。
16. 比较哪个指标受极端错误影响更明显。

### 提高任务

加入 `Sex`：

```text
M
F
I
```

使用 `pd.get_dummies()` 转换后重新训练。

### 最终报告回答

1. MAE 越大越好还是越小越好？
2. RMSE 为什么比 MAE 更容易受到大误差影响？
3. R²=1 表示什么？
4. R² 接近 0 表示什么？
5. 是否应该只看一个指标判断模型？