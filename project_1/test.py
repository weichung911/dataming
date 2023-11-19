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

# import pandas as pd

# # 假设有一个 DataFrame df，其中包含 'transaction_date' 列
# data = {'ID': [1, 2, 3, 4],
#         'transaction_date': ['10/15/2023', '11/02/2023', '11/20/2023', '12/05/2023'],
#         'amount': [100, 150, 200, 120]}

# df = pd.DataFrame(data)

# # 将 'transaction_date' 列转换为日期类型（指定日期格式）
# df['transaction_date'] = pd.to_datetime(df['transaction_date'], format='%m/%d/%Y')

# # 拆分 DataFrame 为 11 月以前和 11 月以后
# before_november = df[df['transaction_date'] < '2023-11-01']
# after_november = df[df['transaction_date'] >= '2023-11-01']

# # 打印结果
# print("Before November:")
# print(before_november)
# print("\nAfter November:")
# print(after_november)
import pandas as pd

# 假设有两个 DataFrame df1 和 df2
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [2, 3, 4], 'Age': [25, 30, 22]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 使用 merge 合并两个 DataFrame
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# 打印合并后的 DataFrame
print(merged_df)


import pandas as pd

# 假设有一个 DataFrame df
data = {'ID': [1, 2, 3], 'Category': [['A', 'C'], ['B', 'D'], ['AB', 'BC']]}
df = pd.DataFrame(data)

# 使用 apply 和 any 找到包含 'A' 的行
result_df = df[df['Category'].apply(lambda x: 'A' in x)]

# 打印包含 'A' 的行
print(result_df)