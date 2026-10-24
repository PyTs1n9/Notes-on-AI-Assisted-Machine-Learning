import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

Path("dataset").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
dataset_dir = Path("dataset")
output_dir = Path("output")
csv_dir = dataset_dir / "Wholesale_customers_data.csv"

df = pd.read_csv(csv_dir, encoding="utf-8-sig")
cols = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
K = 3

scaler = StandardScaler()
standard_data = scaler.fit_transform(df[cols])

model = KMeans(n_clusters=K, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(standard_data)
cluster_profile = (df.groupby("cluster", as_index=False)[cols].mean())
cluster_profile.to_csv(output_dir / "cluster_profile.csv",index=False,encoding="utf-8-sig")
