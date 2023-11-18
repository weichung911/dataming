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
import pandas as pd

import pandas as pd

# 假设有一个 DataFrame df，其中包含 'transaction_date' 列
data = {'ID': [1, 2, 3, 4],
        'transaction_date': ['10/15/2023', '11/02/2023', '11/20/2023', '12/05/2023'],
        'amount': [100, 150, 200, 120]}

df = pd.DataFrame(data)

# 将 'transaction_date' 列转换为日期类型（指定日期格式）
df['transaction_date'] = pd.to_datetime(df['transaction_date'], format='%m/%d/%Y')

# 拆分 DataFrame 为 11 月以前和 11 月以后
before_november = df[df['transaction_date'] < '2023-11-01']
after_november = df[df['transaction_date'] >= '2023-11-01']

# 打印结果
print("Before November:")
print(before_november)
print("\nAfter November:")
print(after_november)

