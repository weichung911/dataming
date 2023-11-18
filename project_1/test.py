import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# 创建示例数据集
data = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 5],
    'Items': ['A, B, D', 'A, C', 'B, D', 'A, B, C', 'B, C, D']
})

# 数据预处理：将逗号分隔的项拆分为单独的项
data['Items'] = data['Items'].str.split(', ')

# 将数据转换为适合mlxtend的格式
data_encoded = pd.get_dummies(data['Items'].explode()).groupby(level=0).sum()
data_encoded = (data_encoded > 0).astype(int)
print(data_encoded)

# 使用Apriori算法获得频繁项集å
frequent_itemsets = apriori(data_encoded, min_support=0.2, use_colnames=True)

# 输出频繁项集
print(frequent_itemsets)

# 根据最小信心生成关联规则
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

# 输出关联规则
print(rules)
