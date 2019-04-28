from sklearn.decomposition import PCA


testlist = [[2, 8, 4, 5],
            [6, 3, 0, 8],
            [5, 4, 9, 1]]

def Pca():
    """
    主成分分析进行特征降维
    :return: None
    """
    pca = PCA(n_components=0.9)

    data = pca.fit_transform(testlist)

    print(data)

    return None

if __name__ == '__main__':
    Pca()