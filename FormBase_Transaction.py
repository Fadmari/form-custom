import pandas as pd
import sqlite3
import formHelper as ff


def form_transaction_base(passoffile, passofbase):
    df = pd.read_excel(passoffile, sheet_name=1, engine='openpyxl') #'Transactions.xlsx'
    df = df.rename({'Идентификатор транзакции':'id_trans', 'Категория товаров, уровень 2':'type_of_product', 'Продукт':'product', 'Вариант товара':'product_variant',
                    'Бренд товара':'type_of_order', 'Количество':'quantity', 'Доход от продукта':'profit'}, axis='columns')

    df = df.fillna('')

    passdb = passofbase[:passofbase.rfind('/')] +'/mybase/customDB.sqlite' #S.rfind(str, [start],[end])
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS TransactionsDB(
       id INT PRIMARY KEY,
       id_trans INT,
       type_of_product TEXT,
       product TEXT,
       product_variant TEXT,
       type_of_order FLOAT,
       quantity INT,
       profit FLOAT);
    """)
    conn.commit()

    for row in range(2, df.shape[0]):
        data = []
        for col in df.columns:
            value = df.at[row, col]
            data.append(value)
        data[0] = float(data[0])
        data[5] = int(data[5])
        cursor.execute("INSERT OR REPLACE INTO TransactionsDB VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (row, data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

    conn.commit()
    conn.close()

# passoffile = '/home/kira/PycharmProjects/pythonProject/data/Analytics.xlsx'
# # savepass = '/home/kira/PycharmProjects/pythonProject/data'
# form_transaction_base(passoffile, passoffile)
# # mycount = service(passoffile)
# # savexcl(savepass, passoffile)
# # print(mycount[0], mycount[1])