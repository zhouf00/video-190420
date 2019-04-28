from sklearn.feature_extraction.text import CountVectorizer


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

    countvec()