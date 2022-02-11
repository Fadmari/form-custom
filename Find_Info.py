import pandas as pd
import sqlite3


def find_transaction(bdpass, number):
    passdb = f"{bdpass}/customDB.sqlite"
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("SELECT id_deal, Custom, tel, order_cost, payment_type FROM OrderDB WHERE num_of_transaction == ?", (number,))
    df = cursor.fetchall()
    conn.close()
    return df

# bdpass = '/home/kira/PycharmProjects/pythonProject/data/mybase'
# number = '312289'
#
# # res = find_transaction(bdpass, number)
# # print(res)
# res = find_transaction(bdpass, number)
# print(res)
