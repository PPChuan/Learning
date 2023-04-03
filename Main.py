import math


# x = 8/20
# y = 7/20
# z = 5/20
# a = -1 * (x * math.log(x, 2) + y * math.log(y, 2) + z * math.log(z, 2))
# print(a)

x = 0.886-2/4.308-2.308/4.308*0.567
y = 5/5.385
print(x)
print(x * y)



# import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# x = load_iris().data
# y = load_iris().target
# x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=2022)
# destree = DecisionTreeClassifier(criterion='gini',splitter='best',max_depth=3,max_leaf_nodes=4) # 选择gini准则即为CART算法  参数max_depth（树的最大深度）和max_leaf_nodes（最大叶节点数） 可以进行剪枝
# dd = destree.fit(x_train,y_train)
# ytest_pre = destree.predict(x_test)
# ytrain_pre = destree.predict(x_train)
# print(f'训练集精确度：{accuracy_score(y_train,ytrain_pre)}')
# print(f'测试集精确度：{accuracy_score(y_test,ytest_pre)}')
#
#
# plt.figure(figsize=(8,6))
# plot_tree(dd)
# plt.show()

