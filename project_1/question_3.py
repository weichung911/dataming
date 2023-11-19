from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import sqlite3
import utilities
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

df = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv',usecols=['customer_id','product_id'])

# transactions = df.groupby(['transaction_date', 'customer_id', 'store_id']).agg({
# 'quantity': 'sum',
# 'product_id': list
# }).reset_index()
# product_list = productid_to_productname(transactions['product_id'])
customer_data = pd.read_csv('P1_Foodmart\Customer-Lookup.csv',usecols=['customer_id','gender','education','homeowner','yearly_income'])
product_data = pd.read_csv('P1_Foodmart\Product-Lookup.csv',usecols=['product_id','product_brand','recyclable','low_fat'])
merge_df = df.merge(customer_data, on='customer_id',how='left')
merge_df = merge_df.merge(product_data, on='product_id',how='left')
merge_df.drop(['customer_id','product_id'], axis=1, inplace=True)
merge_df.replace({1.0: 'Y', np.nan: 'N'}, inplace=True)
print(merge_df.head())
print(len(merge_df))
merge_df_onehot = utilities.multi_attribute(merge_df)
# print(merge_df_onehot.columns)
# title = np.array(merge_df_onehot.columns)
# np.savetxt('q3_titles.csv', title, delimiter=' ', fmt='%s')
# print(title)
frequent_itemsets = apriori(merge_df_onehot,min_support=0.005,use_colnames=True,low_memory=True)
# print(frequent_itemsets)
frequent_itemsets.to_csv('q3_frequent_itemsets.csv')
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
rules.to_csv('q3_rules.csv')
# 按信心降序排序
rules = rules.sort_values(by="confidence", ascending=False)

# result_df = rules[rules['consequents'].apply(lambda x: 'recyclable_Y' in x)]
# print(result_df)
# 输出前10条关联规则
# top_10_confidence_rules = rules.head(10)
# print(top_10_confidence_rules)
# top_10_confidence_rules.to_csv('q3.csv')

