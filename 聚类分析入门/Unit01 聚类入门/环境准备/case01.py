from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
Path("data").mkdir(exist_ok=True)
df = pd.DataFrame({
	"Fresh": rng.integers(1000,10000,50),
	"Milk": rng.integers(500,8000,50),
	"Grocery": rng.integers(1000,12000,50),
	"Frozen": rng.integers(1000,12000,50)
})
df.to_csv("data/wholesale_demo.csv",index=False,encoding="utf-8-sig")
print(df.head())
print("文件存在：", Path("data/wholesale_demo.csv").exists())