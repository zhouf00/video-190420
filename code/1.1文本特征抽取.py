# 导入包
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
my_dic = [{"city": "北京", "temperture": 100},
          {"city": "上海", "temperture": 200},
          {"city": "深圳", "temperture": 30}]

def dictivec():
    """
    字典数据抽取
    :return: None
    """
    # 实例化
    dict = DictVectorizer(sparse=False)

    # 调用fit_transform
    data = dict.fit_transform(my_dic)

    print(dict.get_feature_names())

    print(dict.inverse_transform(data))

    print(data)

    return None

def countvec():
    """
    对文本进行特征值化
    :return:
    """
    cv = CountVectorizer()

    data = cv.fit_transform(["life  is is short, i like python", "life is too long, i dislike python"])

    print(cv.get_feature_names())
    print(data.toarray())
    #print(data)

    return None

if __name__ == '__main__':
    dictivec()
    #countvec()