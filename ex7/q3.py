from pylab import *

# 绘制饼图
n = 20
Z = np.random.uniform(0, 1, n)
pie(Z), show()

# 直方图
fig, ax = plt.subplots(1, 1)
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
ax.hist(a, bins=[0, 25, 50, 75, 100])
ax.set_xticks([0, 25, 50, 75, 100])
show()

# 散点图
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
scatter(X, Y)
show()

# 条形图
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
ylim(-1.25, +1.25)
show()

# 柱状图
data = [5, 20, 15, 25, 10]
plt.bar(range(len(data)), data)
plt.show()
