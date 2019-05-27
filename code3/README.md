# 数据的降维

![例图](https://github.com/zhouf00/video-190420/raw/master/image/d3.1.png)

### 1.特征选择

### 2.主成分分析

> ## 特征选择

	1、特征选择是什么
	2、sklearn特征选择API
	3、其它牲选择方法

**特征选择原因**
	
	冗余：部分特征的相关度高，容易计算性能
	噪声：部分特征对预测结果有影响

**特征选择是什么**

	特征选择就是单纯地从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前和选择后可以改变值、也不改变值，但是选择后的特征
	维数肯定比选择前小，毕竟我们只选择了其中的一部分特征
	主要方法（三大武器）：fllter(过滤式):VarlaneThreshold
						Embedded(嵌入式)：正则化，决策树
						Wrapper(包裹式)
**sklearn特征选择API**

类：sklarn.feature_selection.VariaceThreshold

> ### VarianceThreshold语法

VarianceThreshold(threshold=0.0)

	删除所有所有低方差特征
	Variance.fit_transform(x)
		x：numpy array格式的数据[n_samples, n_features]
		返回值：训练集差异低于threshold的特征将被删除
		默认值是保留所有非零方差特征，即删除所有样本中具有相同值的特征

**VarianceThreshold流程（代码演示）**
	
	1、初始化VarianceThreshold，指定阀值方法
	2、调用fit_transform

**练习1**

	[[0, 2, 0, 3],
     [0, 1, 4, 3],
     [0, 1, 1, 3]]
[练习1代码](https://github.com/zhouf00/video-190420/blob/master/code3/3.1VarianceThreshold.py) 

**其它特征选择方法**

神经网络

	后面具体介绍


> ## sklearn主成分分析API

类：sklearn.decomposition

**PCA是什么**

	本质：PCA是一种分析、简化数据集的技术
	目的：是数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息
	作用：可以削减回归分析或者聚类分析特征的数量
	
	PCA:特征数据达到上百的时候，考虑数据简化
		数据也会改变，特征数据也会减少
**高维度数据容易出现的问题**

特征之间通常是相关的

![二维简化成一维](https://github.com/zhouf00/video-190420/raw/master/image/d3.2.png)

![PCA公式](https://github.com/zhouf00/video-190420/raw/master/image/d3.3.png)


> ### PCA语法

**PCA(n_components=None)**

n_components：<br>小数： 0~1 建议90%-95% <br>整数：减少到的特征数量
	
	将数据分解为较低维数空间
	PCA.fit_transform(x)
		x:numpy array格式的数据[n_sampies,n_features]
		返回值：转换后指定维度的array

**PCA流程（代码演示）**
	
	1、初始化PCA，指定减少后的维度
	2、调用fit_transform

**练习2**

	[[2, 8, 4, 5],
     [6, 4, 0, 8],
     [5, 4, 9, 1]]
[练习2代码](https://github.com/zhouf00/video-190420/blob/master/code3/3.2PCA.py) 

**练习3**

	探究：用户对物品类别的喜好细分降维
	order_products_prior.csv  订单与商品信息
	products.csv  			  商品信息
	orders.csv				  用户的订单信息
	aisles.csv				  商品所属具体物品类别
[练习3代码](https://github.com/zhouf00/video-190420/blob/master/code3/3.3MarketBasket.py) 

**特征选择与主成分分析的比较**

	维度（特征数量）超过几百个的时候，用主成分分析
	

