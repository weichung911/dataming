from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import sqlite3
from utilities import *

df = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')

transactions = df.groupby(['transaction_date', 'customer_id', 'store_id']).agg({
'quantity': 'sum',
'product_id': list
}).reset_index()
product_list = productid_to_productname(transactions['product_id'])
# print(product_list)

te = TransactionEncoder()
te_product_list = te.fit(product_list).transform(product_list)

product_onehot = pd.DataFrame(te_product_list,columns=te.columns_)
print(len(product_onehot))

frequent_itemsets = apriori(product_onehot,min_support=0.00015,use_colnames=True)
print(frequent_itemsets)