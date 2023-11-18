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

transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%m/%d/%Y')
before_December = transactions[transactions['transaction_date'] < '1998-12-01']
after_December = transactions[transactions['transaction_date'] >= '1998-12-01']
print(len(before_December))
print(len(after_December))
before_Decembe_list = productid_to_productname(before_December['product_id'])
# print(before_Decembe_list)
te = TransactionEncoder()
te_before_Decembe_list = te.fit(before_Decembe_list).transform(before_Decembe_list)
te_before_Decembe_onehot = pd.DataFrame(te_before_Decembe_list,columns=te.columns_)
before_Decembe_supoort = apriori(te_before_Decembe_onehot,min_support=0.003,use_colnames=True,low_memory=True)
before_Decembe_supoort = before_Decembe_supoort.sort_values(by="support", ascending=False)
print(before_Decembe_supoort.head())
after_Decembe_list = productid_to_productname(after_December['product_id'])
# print(after_Decembe_list)
te = TransactionEncoder()
te_after_Decembe_list = te.fit(after_Decembe_list).transform(after_Decembe_list)
te_after_Decembe_onehot = pd.DataFrame(te_after_Decembe_list,columns=te.columns_)
after_Decembe_supoort = apriori(te_after_Decembe_onehot,min_support=0.003,use_colnames=True,low_memory=True)
after_Decembe_supoort = after_Decembe_supoort.sort_values(by="support", ascending=False)
print(after_Decembe_supoort.head())
before_Decembe_supoort.to_csv('q4_before.csv', index=False)
after_Decembe_supoort.to_csv('q4_after.csv', index=False)
top_30_before = before_Decembe_supoort.head(10)
top_30_after = after_Decembe_supoort.head(10)

common_data = pd.merge(top_30_before, top_30_after, on='itemsets', how='inner')
different_data_before = top_30_before[~top_30_before['itemsets'].isin(common_data['itemsets'])]
different_data_after = top_30_after[~top_30_after['itemsets'].isin(common_data['itemsets'])]
# 打印结果
print("\nCommon Data:")
print(common_data)
print("\nDifferent Data Before:")
print(different_data_before)
print("\nDifferent Data After:")
print(different_data_after)
common_data.to_csv('q4_Common.csv')
different_data_before.to_csv('q4_dff_before.csv')
different_data_after.to_csv('q4_dff_after.csv')