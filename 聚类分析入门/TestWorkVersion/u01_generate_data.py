import numpy as np
import pandas as pd
import os

rng = np.random.default_rng(20240715)

# 定义 4 个隐含客群的消费画像
# 每行 = [Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen] 的均值
profiles = {
	"A_大体量综合批发商": [2300, 8800, 11800, 3200, 4500, 900],  # 全品类采购，量极大
	"B_门店生鲜专供": [4100, 1400, 2600, 1200, 500, 420],  # 生鲜为主
	"C_乳品清洁日化": [600, 5200, 4200, 700, 3800, 260],  # 乳品+纸品清洁
	"D_小型零售": [1500, 600, 900, 500, 260, 130]  # 全都小
}
weights = [0.22, 0.28, 0.26, 0.24]  # 各客群占比
cols6 = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]

# 按客群分别抽样，合并成 440 行
n = 440
records, true_group = [], []

for (name, mu), w in zip(profiles.items(), weights):
	k = round(w * n) # 这个客群要多少人
	true_group += [name] * k
	m = np.array(mu, dtype=float)
	# 对数正态抽样：乘性波动，模拟真实消费的长尾特征
	draw = rng.lognormal(mean=np.log(m), sigma=0.42, size=(k, 6))
	draw = np.clip(draw, 5, None)  # 消费不会为负
	for row in draw:
		records.append(row)

df = pd.DataFrame(records, columns=cols6).round(0)
df["Channel"] = rng.choice([1, 2], size=n, p=[0.55, 0.45])
df["Region"] = rng.choice([1, 2, 3], size=n, p=[0.42, 0.28, 0.30])
df["True_Group"] = true_group  # 只用于教学验证，不参与建模

df = df[["Channel", "Region", "Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen", "True_Group"]]

# 故意注入脏数据，让单元二有活可干
rng2 = np.random.default_rng(999)
dup_idx = rng2.choice(df.index, size=12, replace=False)  # 12行重复
df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)

nan_idx = rng2.choice(df.index, size=8, replace=False)
df.loc[nan_idx, "Milk"] = np.nan
nan2 = rng2.choice(df.index, size=5, replace=False)
df.loc[nan2, "Grocery"] = np.nan

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(out, exist_ok=True)
df.to_csv(os.path.join(out, "wholesale_customers.csv"),
          index=False, encoding="utf-8-sig")
print(f"[单元一] 数据已生成，总行数（含重复）：{len(df)}")
print(df.head(8).to_string(index=False))
print(df["True_Group"].value_counts().to_string())

