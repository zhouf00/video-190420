import pandas as pd
from sklearn.decomposition import PCA


# 读取四张表的数据
prior = pd.read_csv("../data/order_products_prior.csv")
products = pd.read_csv("../data/products.csv")
orders = pd.read_csv("../data/orders.csv")
aisles = pd.read_csv("../data/aisles.csv")

# 合并四张表到一张表（用户-物品类别）
_mg = pd.merge(prior, products, on=["product_id", "product_id"])
_mg = pd.merge(_mg, orders, on=["order_id", "order_id"])
mt = pd.merge(_mg, aisles, on=["aisle_id", "aisle_id"])
print(mt)

# 交叉表（特殊的分组工具）
cross = pd.crosstab(mt["user_id"], mt["aisle"])
print(cross)

## 进行主成分分析
pca = PCA(n_components=0.9)
data = pca.fit_transform(cross)
#print(data.shape)