# from mlxtend.frequent_patterns import apriori
# from mlxtend.frequent_patterns import association_rules
# from mlxtend.preprocessing import TransactionEncoder

# import pandas as pd

# foodmart_data = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')
# # filtered_df = foodmart_data[foodmart_data['customer_id'] == 2439]
# # print(filtered_df)
# a = TransactionEncoder()
# a_data = a.fit(foodmart_data).transform(foodmart_data)
# print(a.columns_)
# encode_data = pd.DataFrame(a_data,columns=a.columns_)
# encode_data = encode_data.replace(False,0)
# print(encode_data)

# # 使用Apriori算法获得频繁项集
# frequent_itemsets = apriori(encode_data, min_support=0.00015, use_colnames=True)
# print(frequent_itemsets)
# # 根据最小信心生成关联规则
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

# # 按信心降序排序
# rules = rules.sort_values(by="confidence", ascending=False)

# # 输出前10条关联规则
# top_10_confidence_rules = rules.head(10)
# print(top_10_confidence_rules)

# # 根据lift值排序
# rules = rules.sort_values(by="lift", ascending=False)

# # 输出前10条具有最高lift值的关联规则
# top_10_lift_rules = rules.head(10)
# print(top_10_lift_rules)

import pandas as pd
import mlxtend

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Color': ['Red', 'Blue', 'Red', 'Blue', 'Green', 'Red'],
    'Value': [10, 15, 20, 25, 30, 5]
}

df = pd.DataFrame(data)


df = pd.DataFrame(data)

# 使用groupby方法按'Category'列进行分组，并计算每个组的平均值
grouped = df.groupby(['Category','Color'])
# result = grouped.mean()

print(list(grouped))

print(list(grouped)[1][1]['Value'])

# df = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')

# transactions = df.groupby(['transaction_date', 'customer_id', 'store_id']).agg({
# 'quantity': 'sum',
# 'product_id': list
# }).reset_index()

# print(transactions)
# date_index = transactions['transaction_date'].index[transactions['transaction_date'] == '12/14/1998']

# print(date_index)
import pandas as pd
import utilities

# 提供的数据，包含多个属性
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Color': ['Red', 'Blue', 'Red', 'Blue', 'Green', 'Red'],
    'Size': ['Small', 'Large', 'Medium', 'Small', 'Large', 'Medium'],
    'Shape': ['Square', 'Circle', 'Square', 'Circle', 'Square', 'Circle'],
}
# 创建数据框
df = pd.DataFrame(data)
utilities.multi_attribute(df)
# # 将多个属性合并为一个新的列
# df['Combined'] = df['Category'] + '_' + df['Color'] + '_' + df['Size'] + '_' + df['Shape']
# col = df.columns
# print(df.columns)
# # 使用透视表生成以属性组合为列的表格
# pivot_table = df.pivot_table(index=data, columns=['Category','Color'], aggfunc = 'size',fill_value=0)

# # 重新设置列名

# pivot_table.columns = [f"{col[0]}_{col[1]}_{col[2]}" if len(col) == 3 else f"{col[0]}_{col[1]}" for col in pivot_table.columns]


# # 重置索引，将多层索引转换为单层索引
# pivot_table.reset_index(inplace=True)

# 打印真值表
# print(pivot_table)
import pandas as pd

# 假设有一个 DataFrame df
data = {'ID': [1, 2, 3], 'Category': [['A', 'C'], ['B', 'D'], ['AB', 'BC']]}
df = pd.DataFrame(data)

# 使用 apply 和 any 找到包含 'A' 的行
result_df = df[df['Category'].apply(lambda x: 'A' in x)]

# 打印包含 'A' 的行
print(result_df)

import pandas as pd

# 假设有一个 DataFrame df
data = {'ID': [1, 2, 3], 'Category': [['A', 'C'], ['B', 'D'], ['AB', 'BC']]}
df = pd.DataFrame(data)

# 使用 apply 和 any 找到包含 'A' 或 'B' 的行
result_df = df[df['Category'].apply(lambda x: any(category in ['A', 'B'] for category in x))]

# 打印包含 'A' 或 'B' 的行
print(result_df)

