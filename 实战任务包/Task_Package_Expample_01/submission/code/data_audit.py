import pandas as pd
import numpy as np

df_day = pd.read_csv(
	'D:\\Code\\Python\\人工智能基础\\实战任务包\\Task_Package_Expample_01\\data\\bike_sharing\\day.csv')
df_hour = pd.read_csv(
	'D:\\Code\\Python\\人工智能基础\\实战任务包\\Task_Package_Expample_01\\data\\bike_sharing\\hour.csv')

for _ in [df_day, df_hour]:
	print(f'{_} 形状：', _.shape)
	print(f'{_} 字段名称：', _.columns)
	print(f'{_} 字段类型：', _.dtypes)
	print(f'{_} head信息：', _.head())
	print(f'{_} describe信息：', _.describe())
	print(f'{_} 每列缺失值数量：', _[_.columns].isnull().sum())
	print(f'{_} 完全重复行数量：', _.duplicated().sum())
	print(f'{_} instant列重复情况：', _['instant'].duplicated().sum())
key_cols = ["dteday", "hr"]
print(f'{_} 日期键重复情况：', _.duplicated(subset=key_cols, keep="first").sum())


def make_rows(df, name):
	rows = []
	for col in df.columns:
		s = df[col]
		if s.dtype in ['int64', 'float64']:
			s_max = s.max()
			s_min = s.min()
			s_mean = s.mean()
			s_std = s.std()
		else:
			s_max = s_mean = s_min = s_std = np.nan

		rows.append({
			'dateset': name,
			'column': col,
			'shape': s.shape,
			'dtype': s.dtype,
			'max': s_max,
			'min': s_min,
			'mean': s_mean,
			'std': s_std,
			'missing': s.isnull().sum(),
			'non-null': s.notna().sum(),
			'duplicated': s.duplicated().sum()

		})
	return rows


table = []

table += make_rows(df_day, "day")
table += make_rows(df_hour, "hour")

data_profile = pd.DataFrame(table)
data_profile.to_csv('../data_outputs/data_profile.csv', encoding='utf-8-sig', index=False)

stats_cols = ['cnt', 'temp', 'hum', 'windspeed']
df_stats = df_day[stats_cols].describe().T
df_stats.to_csv('../data_outputs/df_day_stats.csv', encoding='utf-8-sig')
df_stats = df_hour[stats_cols].describe().T
df_stats.to_csv('../data_outputs/df_hour_stats.csv', encoding='utf-8-sig')

all_outlier = pd.DataFrame()


def outlier_tool(df, name):
	global all_outlier
	s = df['cnt']
	Q1 = s.quantile(0.25)
	Q3 = s.quantile(0.75)
	IQR = Q3 - Q1
	lower_bound = Q1 - 1.5 * IQR
	upper_bound = Q3 + 1.5 * IQR
	outlier_df = df[(df['cnt'] < lower_bound) | (df['cnt'] > upper_bound)].copy()
	outlier_df['dataset'] = name
	all_outlier = pd.concat([all_outlier, outlier_df], ignore_index=True)


outlier_tool(df_day, "day")
outlier_tool(df_hour, "hour")
all_outlier.to_csv('../data_outputs/outlier_candidates.csv', encoding='utf-8-sig', )

print('输出True说明满足cnt == casual + registered ', (df_day['casual'] + df_day['registered'] == df_day['cnt']).all())
print('输出True说明满足cnt == casual + registered ', (df_hour['casual'] + df_hour['registered'] == df_hour['cnt']).all())

day = df_day.copy()
hour = df_hour.copy()
day.to_csv('../data_outputs/day_clean.csv', encoding='utf-8-sig', index=False)
hour.to_csv('../data_outputs/hour_clean.csv', encoding='utf-8-sig', index=False)
