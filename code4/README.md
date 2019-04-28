# 机器学习算法

## sklearn数据集

	1、数据集划分
	2、sklearn数据集接口介绍
	3、sklearn分类数据集
	4、sklearn回归数据集

## 转换器与预估器

> ## 转换器

![转换器](https://github.com/zhouf00/video-190420/raw/master/image/d47.png)

> ## sklearn机器学习算法的实现-估计器

**在sklearn中，估计（estimator）是一个重要的角色，是一类实现了算法的API**

	1、用于分类的估计器：
		sklearn.neghbors  K-近邻算法
		sklearn.naive_bayes  贝叶斯
		sklearn.linear_model.LogisticRegression  逻辑回归
		sklearn.tree  决策树与随机森林
	2、用于回归的估计器：
		sklearn.linear_model.LinearRegression  线性回归
		sklearn.linear_model.Ridge  岭回归

> ## k-近邻算法以及案例预测入住位置

**[k-近邻算法代码](https://github.com/zhouf00/video-190420/blob/master/code4/4_k_neighbors.py)**

> ## 决策树

**sklearn决策树API**
	
	class sklearn.tree.DecisionTreeClassifier(criterion='gini', max_depth=None, random_state=None)
		决策树分类器
		criterion：默认是'gini'系数，也可以选择信息增益的熵'entropy'
		max_depth：树的深度大小
		random_state：随机种子

		method：
		decision_path：返回决策树的路径

![决策树](https://github.com/zhouf00/video-190420/raw/master/image/d48.png)

**[决策树代码](https://github.com/zhouf00/video-190420/blob/master/code4/4_tree.py)**