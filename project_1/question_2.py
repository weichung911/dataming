from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import sqlite3
import utilities
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

customer_data = pd.read_csv('P1_Foodmart\Customer-Lookup.csv',usecols=['customer_state_province','yearly_income','gender','total_children','num_children_at_home','education','occupation','homeowner'])
print(customer_data.head())
print(len(customer_data))
customer_onehot = utilities.multi_attribute(customer_data)
print(customer_onehot.columns)
# te_interst = te.fit(interest_data).transform(interest_data)
frequent_itemsets = apriori(customer_onehot,min_support=0.05,use_colnames=True,low_memory=True)
print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.9)
# 按信心降序排序
rules = rules.sort_values(by="confidence", ascending=True)

# 输出前10条关联规则
top_10_confidence_rules = rules.head(10)
print(top_10_confidence_rules['antecedents'])
# top_10_confidence_rules.to_csv('q2_top_10_confidence.csv', index=False)

# interest_onehot = pd.DataFrame(te_interst,columns=te.columns_)
# print(interest_onehot.columns)