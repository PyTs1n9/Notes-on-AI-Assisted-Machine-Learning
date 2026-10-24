# 人工智能基础 · 学习仓库

机器学习入门自学记录：课程文档、逐行注释代码、练习与考核、学习思路。主线是「回归预测」与「聚类分析」两个算法方向，穿插 Pandas 数据分析和 matplotlib 可视化基本功。

## 目录介绍

### 自主学习/
按课次编排的主学习线，每课一个文件夹（课程 markdown + 示例代码 + 练习），当前进度：
- 第一课～第二课：线性回归入门、train_test_split 训练集与测试集划分
- 第三课～第四课：Pandas 入门（Series / DataFrame）、取数（loc / iloc / 条件筛选）与 CSV 读写
- 第五课：回归评价指标（MAE、MSE、RMSE、R²）
- 单元测试①：回归入门与 Pandas 基础（回滚复盘 + 综合练习）

### 回归预测入门/
回归方向的单元式练习与阶段考核：
- `Unit01～Unit06/`：训练/验证集划分、线性回归预测、岭回归与正则化、Lasso 与特征选择、评价指标（RMSE/MAE/R²）、交叉验证。每个单元含 case 示例、练习、目标说明（goals.txt）和产出报告
- `Test题目/Test01～Test05/`：阶段考核（题目文档 + 代码 + 数据集 + 输出结果 + report.md）

### 聚类分析入门/
聚类方向（无监督学习）的单元式练习与实战：
- `Unit01～Unit08/`：KMeans 入门、客户分群任务理解与数据清理、StandardScaler 标准化、KMeans 训练、肘部法则、轮廓系数、Davies-Bouldin 指数、聚类可视化
- `TestWorkVersion/`：wholesale 客户分群实战手册——从生成数据到业务报告的 10 单元完整项目
- `Test题目/Test01～Test04/`：阶段考核（KMeans 入门、肘部法则、轮廓系数与 DBI、客户画像解释）

### 可视化入门①/ 与 可视化入门②/
matplotlib 图表入门，各含 8 种基础图表（折线图、柱状图、横向柱状图、散点图、饼图、直方图、箱线图、热力图），每种图一个文件夹（`example.py` 示例 + `test.py` 练习 + 参考图）：
- ①基础版：只讲「能画出图」的最小必要内容
- ②进阶版：注释覆盖每个参数，练习题含 TODO 待填代码与参考答案

### .hermes.md
学习规划与教学约定：学习路径、单元测试机制、课程文档管理规则。

## 运行环境

- Python 3.10+
- 依赖：`numpy`、`pandas`、`scikit-learn`、`matplotlib`

## License

[MIT](LICENSE) © 2026 PyTs1N9
