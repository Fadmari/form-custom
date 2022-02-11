import pandas as pd
import sqlite3
import formHelper as ff


def form_order_base(passoffile, passofbase):
    df = pd.read_excel(passoffile, engine='openpyxl') #'Orders.xlsx'
    df = df.rename({'№':'id_deal', 'Номер заказа':'Order_id', 'Клиент':'Custom', 'Телефон клиента':'tel', 'Сумма':'order_cost', 'Форма оплаты':'payment_type',
                        'Итого поступило':'Итого поступило', 'Дата оплаты 1':'date_of_bye'}, axis='columns')
    # df['date_of_bye'] = df['date_of_bye'].dt.date
    # df['real_deal'] = df['real_deal'].fillna(value=0)
    df = df.fillna('')

    passdb = passofbase[:passofbase.rfind('/')] +'/mybase/customDB.sqlite' #S.rfind(str, [start],[end])
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS OrderDB(
       id INT PRIMARY KEY,
       id_deal TEXT,
       Order_id TEXT,
       Custom TEXT,
       tel TEXT,
       order_cost FLOAT,
       payment_type TEXT,
       итого_поступило TEXT,
       date_of_bye TEXT,
       num_of_transaction);
    """)
    conn.commit()

    for row in range(2, df.shape[0]):
        data = []
        for col in df.columns:
            value = df.at[row, col]
            data.append(value)
        # data[0] = int(data[0])
        # ff.form_type(data)
        ff.form_tel(data, 3)
        ff.form_order_num(data, 1)
        # ff.form_name(data)
        # ff.form_gender(data)
        cursor.execute("INSERT OR REPLACE INTO OrderDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (row, data[0], data[1], data[2],
                                                                                          data[3], data[4], data[7],
                                                                                          data[8], data[11], data[13]))

    conn.commit()
    conn.close()

# passoffile = '/home/kira/PycharmProjects/pythonProject/data/Orders.xlsx'
# # savepass = '/home/kira/PycharmProjects/pythonProject/data'
# form_order_base(passoffile)
# # mycount = service(passoffile)
# # savexcl(savepass, passoffile)
# # print(mycount[0], mycount[1])