import matplotlib.pyplot as plt

plt.scatter([1, 1.2, 5, 5.2],
            [1, 1.1, 5, 5.1],
            c=[0, 0, 1, 1],
            cmap="viridis")

plt.xlabel("鲜品消费")
plt.ylabel("奶类消费")
plt.title("二维客户分群")
plt.show()
