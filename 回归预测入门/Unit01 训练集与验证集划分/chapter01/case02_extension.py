import pandas as pd
from pathlib import Path
import numpy as np

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

# 假设 df 已经存在
# 每 50 条数据划分为一个批次
df["Batch"] = np.arange(len(df)) // 50 + 1

# 统计每个批次的数量

batch_counts = df["Batch"].value_counts().sort_index()
print(batch_counts)


df.to_csv(
    "data/rings_train_with_batch.csv",
    index=False,
    encoding="utf-8-sig"
)















