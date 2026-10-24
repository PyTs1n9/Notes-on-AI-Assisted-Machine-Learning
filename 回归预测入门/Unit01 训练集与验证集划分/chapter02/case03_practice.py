# 把 X 换成 rings 数据的 7 个测量字段；
# 把 Rings 设为 y；
# 检查两边长度一致；
# 最后打印训练和验证行数。
# 不要将 Rings 自身放入 X，也不要将敏感编号放入 X。

# 作用： 生成数据、清理重复和已知人造异常、填补空值、拆分并保存划分信息。
# 运行后看到： data/rings_train.csv 与 reports/split_info.txt。请检查两个路径。

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)
n = 300
length = rng.uniform(.2,.8,n)
whole = length * 2.2 + rng.normal(0,.15,n)
cols = ["Length", "Diameter", "Height", "Whole_weight",
		"Shucked_weight", "Viscera_weight", "Shell_weight"]
df = pd.DataFrame({
	"Length": length,
	"Diameter": length*.8,
	"Height": length*.18,
	"Whole_weight": whole,
	"Shucked_weight": whole*.45,
	"Viscera_weight": whole*.2,
	"Shell_weight": whole*.3,
	"Rings": np.rint(2 + 8*length + 2*whole +
			rng.normal(0, 1.2, n)),
	"Sensitive_ID": [f"ID-{i}" for i in range(n)]
})

df.loc[3, "Height"] = np.nan
df = pd.concat([df, df.iloc[[10]]], ignore_index=True)
df.loc[20, "Height"] = 9.99

df = df.drop_duplicates()
df = df[df["Height"] < 1.0].copy() # 本例确认该行是人造错误后删除
df[cols] = df[cols].fillna(df[cols].median())

X, y = df[cols], df["Rings"]
X_train, X_val, y_train, y_val = train_test_split(
X, y, test_size=0.2, random_state=42
)

text = (f"总样本：{len(df)}\n训练样本：{len(X_train)}\n"
f"验证样本：{len(X_val)}\n随机种子：42\n")
Path("reports/split_info.txt").write_text(text, encoding="utf-8")
print(text)






