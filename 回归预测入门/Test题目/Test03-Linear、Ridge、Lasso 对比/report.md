# Linear、Ridge、Lasso 的测试结果是否明显不同？
> Linear无正则化，系数大了可能过拟合
> Ridge系数缩小但是不会归零，RMSE较稳定
> Lasso系数可能归零，alpha正则化大时RMSE急剧上升

# alpha 太大后会发生什么？
> 惩罚过重，系数拉低，预测不准确

# 哪些葡萄酒特征对 quality 影响较明显？
> 根据coef绝对值判断，值越大影响越明显
> 所以alcohol，density 对quality影响明显

# Lasso 为什么可能把某些系数压缩为 0？
> 系数很小的时候，绝对值惩罚会直接把系数压到0，直接筛掉
