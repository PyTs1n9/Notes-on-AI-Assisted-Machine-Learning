import pandas as pd

df = pd.DataFrame({
	"Fresh": [100, 200],
	"Milk": [20, 40],
	"Customer_ID": ["A01", "A02"],
	"类型答案": ["甲", "乙"]
})
X = df[["Fresh", "Milk"]]
print(X)
