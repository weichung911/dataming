import pandas as pd
from sqlalchemy import create_engine

transaction_data = pd.read_csv('P1_Foodmart/FoodMart-Transactions-1998.csv')
customer_data = pd.read_csv('P1_Foodmart/Customer-Lookup.csv')
product_data = pd.read_csv('P1_Foodmart/Product-Lookup.csv')

engine = create_engine('sqlite:///Foodmark_data.db')
transaction_data.to_sql('Transactions', con=engine, if_exists='replace', index=False)
customer_data.to_sql('customer-Lookup', con=engine, if_exists='replace', index=False)
product_data.to_sql('Product-Lookup', con=engine, if_exists='replace', index=False)