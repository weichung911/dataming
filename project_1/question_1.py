from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import sqlite3
from utilities import *
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

df = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')

transactions = df.groupby(['transaction_date', 'customer_id', 'store_id']).agg({
'quantity': 'sum',
'product_id': list
}).reset_index()
product_list = productid_to_productname(transactions['product_id'])
# product_list = transactions['product_id']
# print(product_list)

te = TransactionEncoder()
te_product_list = te.fit(product_list).transform(product_list)

product_onehot = pd.DataFrame(te_product_list,columns=te.columns_)
# print(len(product_onehot))
# print(product_onehot.shape)
frequent_itemsets = apriori(product_onehot,min_support=0.00015,use_colnames=True,low_memory=True)
# print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
# 按信心降序排序
rules = rules.sort_values(by="confidence", ascending=False)

# 输出前10条关联规则
top_10_confidence_rules = rules.head(10)
top_10_confidence_rules.to_csv('q1_top_10_confidence.csv', index=False)

# 根据lift值排序
rules = rules.sort_values(by="lift", ascending=False)

# 输出前10条具有最高lift值的关联规则
top_10_lift_rules = rules.head(10)
top_10_lift_rules.to_csv('q1_top_10_lift.csv', index=False)
print(top_10_lift_rules)