# sklearn特征抽取API

- ### sklarn.feature_extraction ###
	> ## 字典特征抽取

		作用：对字典数据进行特征值化
		
		类：sklarn.feature_extraction.DictVectorizer
	
	> ## DictVectorizer语法

	**DictVectorizer (sparse=True, ...)**

		DictVectorizer.fit_transform(x)
		 	x:字典或者包含字典的迭代器
			返回值：返回sparse矩阵
		DictVectorizer.inverse_transform(x)
			x:array数组或者sparse矩阵
			返回值：转换之前数据格式
		DictVectorizer.get_feature_names()
			返回类别名称
		DictVectorizer.transform(x)
			按照原先的标准转换
		

	**流程**
		
		1.实例化类DictVectorizer
		2.调用fit_transform方法输入数据并转换

	**练习题1**

		[{"city": "北京", "temperture": 100}, 
         {"city": "上海", "temperture": 200}, 
         {"city": "深圳", "temperture": 30}]
		
	[练习题1代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code/1.1%E6%96%87%E6%9C%AC%E7%89%B9%E5%BE%81%E6%8A%BD%E5%8F%96.py)

	![image](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/note3.png)

	> ## CountVectorizer语法

		类：sklearn.feature_extraction.text.CountVectorizer

	**CountVectorizer()  --不支持中文**
	
	文本分类、情感分析
		
		返回词频矩阵
		CountVectorizer.fit_transform()
			x:文本或者包含文本字符串的可迭代对象
			返回值：返回sparse矩阵
		CountVectorizer.inverse_transform(x)
			x:array数据或者sparse矩阵
			返回值：转换之前数据格式
		CountVectorizer.get_feature_names()
			返回值：单词列表
	**流程**
		
		1.实例化类CountVectorizer
		2.调用fit_transform方法输入数据并转换
		**注意返回格式，利用toarray()矩阵转换array数组**
	
	**练习题2**

		["life  is is short, i like python", 
		"life is too long, i dislike python"]
	[练习题2代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code/1.2%E6%96%87%E6%9C%AC%E7%89%B9%E5%BE%81%E6%8A%BD%E5%8F%96.py)

	![image](https://github.com/zhouf00/python-DataStudy/raw/master/video_LM/image/note1.png)

	> ## jieba分词

	**jieba() --中文处理**

		import jieba
		jieba.cut("我是一个好程序员")

		返回值：词语生成器
	**练习题3**

		1、今天很残酷，明天更残酷，后天很美好
		但绝对大部分是死在明天晚上，所以每个人不要放弃今天
		2、我们看到的从很远星系统来的光是在几百万年之前发出的，
		这样当我们看到宇宙时，我们是在看它的过去
		3、如果只用一种方式了解某样事物，你就不会真正了解它。
		了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系
	[练习题3代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code/1.3%E6%96%87%E6%9C%AC%E7%89%B9%E5%BE%81%E6%8A%BD%E5%8F%96_%E4%B8%AD%E6%96%87%E5%A4%84%E7%90%86.py)

	> ## TF-IDF
	
		TF-IDF的主要思想是：如果某个词或短语在一篇文章中出现的概率高，并且在其他文章中很少出现，
		则认为此词或者短语具有很好的类别区分能力，适合用来分类
	
		TF-IDF作用：用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程序
	
		类：sklearn.feature_extraction.text
	> ## TfidfVectorizer语法

	**TfidfVectorizer**
	
		返回词的权重矩阵
		TfidfVectorizer.fit_transform(x)
			x:文本或者包含文本字符串的可迭代对象
			返回值：返回sparse矩阵
		TfidfVectorizer.inverse_transform(x)
			x:array数组或者sparse矩阵
			返回值：转换之前数据格式
		TfidfVectorizer.get_feature_names()
			返回值：单词列表
	**练习题4**

		练习三基础上进行tfidf处理
	[练习题4代码](https://github.com/zhouf00/python-DataStudy/blob/master/video_LM/code/1.4Tfidf.py)