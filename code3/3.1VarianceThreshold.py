from sklearn.feature_selection import VarianceThreshold


testlist = [[0, 2, 0, 3],
            [0, 1, 4, 3],
            [0, 1, 1, 3]]

def Var():
    """
    特征选择-删除低方差的特征
    :return: None
    """
    var = VarianceThreshold(threshold=1.0)

    data = var.fit_transform(testlist)

    print(data)

    return None


if __name__ == '__main__':
    Var()