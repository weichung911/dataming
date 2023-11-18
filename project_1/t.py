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

df = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')

transactions = df.groupby(['transaction_date', 'customer_id', 'store_id']).agg({
'quantity': 'sum',
'product_id': list
}).reset_index()

print(transactions)
date_index = transactions['transaction_date'].index[transactions['transaction_date'] == '12/14/1998']

print(date_index)
