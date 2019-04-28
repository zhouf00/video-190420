from sklearn.preprocessing import StandardScaler

testlist = [[1., -1., 3.],
            [2., 4., 2.],
            [4., 6., -1.]]

def stand():
    """
    标准化缩放
    :return: None
    """
    std = StandardScaler()
    data = std.fit_transform(testlist)
    print(data)


if __name__ == '__main__':
    stand()