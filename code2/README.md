# 数据的特征预处理


### 1.特征处理的方法

### 2.sklearn特征预处理API

> ## 特征处理是什么

	通过特定的统计方法（数字方法）将数据转换成算法要求的数据 

## 特征处理的方法

	数值型数据：标准缩放：
			   1.归一化
			   2.标准化
			   3.缺失值
	类别型数据：one-hot编码
	时间类型：时间的切分

## sklearn特征处理API

**类：sklearn.preprocessing**	
<br>
![归一化](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/1.png)
<br>
![归一化](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/2.png)
<br>

> ## sklearn归一化API

	类：sklearn.preprocessing.MinMaxScaler

> ### MinMaxScaler语法

**MinMaxScaler(feature_range=(0,1)…)**

	每个特征绽放到给定范围（默认[0,1]）
	MinMaxScaler.fit_transform(x)
		x：numpy array格式的数据[n_samples,n_features]
		返回值：转换后的开关相同的array

**归一化步骤**

	1、实例化MinMaxScalar
	2、通过fit_transform转换

**练习1**

	[[90, 2, 10, 40],
 	[60, 4, 15, 45],
 	[75, 3, 13, 46]]
[练习1代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code2/2.1MinMaxScalar.py)

**练习2**

	相亲约会对象数据，这个样本是男士的数据。三个特征，玩游戏所消耗时间的百分比、每年获得的飞行常客里
	程数、每周消费的冰淇淋公升数。然后有一个所属类别，被女士评价的三个类别，不喜欢didnt、魅力一般
	small、极具魅力large也就是说飞行里程数对于结算结果或者说相亲结果影响圈套，但是统计的人觉得这三
	个特征同等重要
		里程数		公升数		消耗时间比			评价
		14488		7.153469	1.673904			smalldoses
		26052		1441871		0.805124			didntLike
[练习2代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code2/2.2MinMaxScalar.py)

**归一化总结**
	
	注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景

**结合归一化来谈标准化**

	对于归一化来说：如果出现异常点，影响了最大值和最小值，那么结果显然会发生改变
	对于标准化来说：如果出现异常点，由于具有一定数据量，少量的异常点对于平均值的影响并不大，从而方差改变较小 

![结合归一化谈标准化](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/4.png)
<br>
![标准化公式](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/3.png)
<br>

> ## sklearn标准化API

	类：sklearn.preprocessing.StandarScaler

> ### StandarScaler语法

**StandardScaler(…)**
	
		处理之后每列来说所有数据都聚焦在均值0附近标准差为1
		StandardScaler.fit_transform(x)
			x：numpy array格式的数据[n_samples,n_features]
			返回值：转换后的开关相同的array
		StandardScaler.mean_
			原始数据中每列特征的平均值
		StandardScaler.std_
			原始数据每列特征的方差
**标准化步骤**

	1、实例化StandarScaler
	2、通过fit_transform转换
**练习3**

	[[1., -1., 3.],
     [2., 3., 2.],
     [4., 6., -1.]]
[练习3代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code2/2.3StandarScaler.py)