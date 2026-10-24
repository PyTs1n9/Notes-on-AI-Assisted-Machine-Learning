## Silhouette Score 与 Davies-Bouldin

继续使用 Wholesale Customers。

### 训练任务

对 K=2～10：

1. 计算 inertia。
2. 计算 silhouette score。
3. 计算 Davies-Bouldin Index。
4. 创建表：

| K | Inertia | Silhouette | DBI |
|---|---:|---:|---:|

5. 保存 `k_metrics.csv`。
6. 绘制三张曲线图。
7. 找：
   - Silhouette 最大 K；
   - DBI 最小 K；
   - Elbow 推荐 K。
8. 如果三个指标不一致，不允许简单写“选最大的”。
9. 综合选择一个 K。
10. 写 300 字说明选择理由。

### 重点问答

1. Silhouette 越大还是越小越好？
2. DBI 越大还是越小越好？
3. 为什么 K 越大 inertia 几乎一定越小？
4. 因此能不能直接选择 inertia 最小的 K？
