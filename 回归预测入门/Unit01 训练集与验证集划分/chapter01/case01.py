# 作用： 生成 100 条简单数据，保存后再读入。
# 运行后看到： 控制台出现五行表格，data/rings_demo.csv 文件生成。
# 请打开文件确认。

from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)
length = rng.uniform(0.2, 0.8, 200)
rings = 3 + 10 * length + rng.normal(0, 1, 200)
Diameter = length * 0.8

df = pd.DataFrame({
	"Length": length,
	"Diameter": Diameter,
	"Rings": rings
})

df.to_csv("data/rings_demo.csv", index=False)

check_df = pd.read_csv("data/rings_demo.csv")

print(check_df.head())
print("行数 ", len(check_df))
print("列名 ", check_df.columns.tolist())
print("缺失值数量 ")
print(check_df.isnull().sum())
