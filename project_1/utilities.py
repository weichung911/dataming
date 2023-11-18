import sqlite3
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

def turple_to_list(turple):
    list = []
    for i in turple:
        list.append(i[0])
    return list

def unique(list):
    li = []
    for i in list:
        if i not in li:
            li.append(i)
    return li

def productid_to_productname(data):
    conn = sqlite3.connect('Foodmark_data.db')
    new_data = []
    cursor = conn.cursor()
    for transaction in data:
        e = []
        for element in transaction:
            sql = f"SELECT product_name FROM 'Product-Lookup' WHERE product_id = {element}"
            cursor.execute(sql)
            product_name = cursor.fetchall()
            product_name = turple_to_list(product_name)
            if product_name != []:
                e.append(product_name[0])
        new_data.append(e)
    conn.close()
    return new_data

def multi_attribute(data: pd.DataFrame) -> pd.DataFrame:
    col = data.columns
    print(col)
    merge_df = pd.DataFrame()
    for c in col:
        li = [[i] for i in data[c]]
        # li.append(list(data[c]))
        # print(li)
        te = TransactionEncoder()
        te_c = te.fit(li).transform(li)
        new_te_c = [str(c)+'_'+ str(s) for s in te.columns_]
        c_onehot = pd.DataFrame(te_c,columns=new_te_c)
        merge_df = pd.concat([merge_df,c_onehot],axis=1)
    # print(merge_df)
    return merge_df


# def create_apriori_datastructure(dataframe, id=False):
#     ############################################
#     # Preparing ARL Datastructure (Invoice-Product Matrix)
#     ############################################

#     # We need to create below structure:

#     # Rows represents transactions (invoice, shopping cart etc.), columns represents products
#     # We simulate as binary that which transaction (invoice, shopping cart etc.) contains which products
#     # If the product is in the invoice, the intersection cell will be "1". If is not, it will be "0"

#     # Description   Product1   Product2    Product3
#     # Invoice
#     # Invoice1          0         1          0
#         # Invoice2          1         0          1
#     # Invoice3          0         0         0
#     # Invoice4          1         0         0
#     # Invoice5          0         0         1
#     if id:
#         grouped = germany_df.groupby(
#             ['Invoice', 'StockCode'], as_index=False).agg({'Quantity': 'sum'})
#         apriori_datastructure = pd.pivot(data=grouped, index='Invoice', columns='StockCode', values='Quantity').fillna(
#             0).applymap(lambda x: 1 if x > 0 else 0)
#         return apriori_datastructure
#     else:
#         grouped = germany_df.groupby(
#             ['Invoice', 'Description'], as_index=False).agg({'Quantity': 'sum'})
#         apriori_datastructure = pd.pivot(data=grouped, index='Invoice', columns='Description', values='Quantity').fillna(
#             0).applymap(lambda x: 1 if x > 0 else 0)
#         return apriori_datastructure