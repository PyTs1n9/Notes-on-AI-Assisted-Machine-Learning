# 生成鲍鱼风格数据；
# 加入空值、重复行、明显异常 Height 和 Sensitive_ID；
# 打印这些问题的数量，
# 保存到 data/rings_train.csv。
# 训练模型时不使用 Sensitive_ID。

from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
Path("data").mkdir(exist_ok=True)

n = 300
length = rng.uniform(0.2, 0.8, n)
whole = 2.2 * length + rng.normal(0, 0.15, n)

df = pd.DataFrame(
	{
		"Sex": rng.choice(["M", "F", "I"], n),
		"Length": length,
		"Diameter": length * 0.8,
		"Height": length * 0.18,
		"Whole_weight": whole,
		"Shucked_weight": whole * 0.45,
		"Viscera_weight": whole * 0.2,
		"Shell_weight": whole * 0.3,
		"Rings": np.clip(np.rint(2 + 8 * length + 2 * whole + rng.normal(0, 1.2, n)),1,None),
		"Sensitive_ID": [f"ID-{i:04d}" for i in range(n)]
	}
)

df.loc[5, "Height"] = np.nan
df.loc[8, "Whole_weight"] = np.nan
pd.concat([df,df.iloc[[10,11]]],ignore_index=True)
df.loc[20, "Height"] = 9.99
df.to_csv("data/rings_train.csv", index=False, encoding="utf-8-sig")

print("数据形状：", df.shape)
print("每列缺失数：\n", df.isna().sum())
print("重复行：", df.duplicated().sum())
print("检查文件：", Path("data/rings_train.csv").exists())

