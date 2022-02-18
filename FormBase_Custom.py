import pandas as pd
import sqlite3
import formHelper as ff



def form_custom_base(passoffile):
    df = pd.read_excel(passoffile, engine='openpyxl') #'Custom.xlsx'
    df = df.rename({'Клиенты':'clients', 'Фамилия':'surname', 'Имя':'name', 'Отчество':'patronymic', 'Телефоны':'tel', 'Почта':'mail',
                        'Активные сделки':'real_deal', 'Дата последней покупки':'last buy', 'Тип клиента':'client type'}, axis='columns')
    df['last buy'] = df['last buy'].dt.date
    # df['real_deal'] = df['real_deal'].fillna(value=0)
    df = df.fillna('')

    passdb = passoffile[:passoffile.rfind('/')] +'/mybase/customDB.sqlite' #S.rfind(str, [start],[end])
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customDB(
       userid INT PRIMARY KEY,
       client TEXT,
       surname TEXT,
       username TEXT,
       patronymic TEXT,
       gender TEXT,
       tel TEXT,
       mail TEXT,
       real_deal INT,
       last_buy TEXT,
       client_type TEXT);
    """)
    conn.commit()

    for row in range(2, df.shape[0]):
        data = []
        for col in df.columns:
            value = df.at[row, col]
            data.append(value)
        data[6] = int(data[6])
        ff.form_type(data)
        ff.form_tel(data, 4)
        ff.form_name(data)
        ff.form_gender(data)
        cursor.execute("INSERT OR REPLACE INTO customDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (row, data[0], data[1], data[2],
                                                                                          data[3], data[9], data[4], data[5],
                                                                                          data[6], data[7], data[8]))

    conn.commit()
    conn.close()


def service(passoffile):
    passdb = passoffile[:passoffile.rfind('/')] +'/mybase/customDB.sqlite'
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(userid) from customDB")
    rowcount = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(userid) from customDB WHERE client_type == 'Юридическое лицо'")
    urcount = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(userid) from customDB WHERE client_type == 'Физическое лицо'")
    fizcount = cursor.fetchone()[0]

    conn.close()
    return [rowcount, urcount, fizcount]



def savexcl(savepass, passoffile):
    passdb = passoffile[:passoffile.rfind('/')] +'/mybase/customDB.sqlite'
    conn = sqlite3.connect(passdb)
    df = pd.read_sql_query("SELECT * from customDB", conn)

    writer = pd.ExcelWriter(f"{savepass}/Custom.xlsx") #f"{savepass}/Result.xlsx"
    df.to_excel(writer, 'Клиенты')
    writer.save()

    df2 = pd.read_sql_query("SELECT * from OrderDB", conn)
    writer = pd.ExcelWriter(f"{savepass}/Orders.xlsx")  # f"{savepass}/Result.xlsx"
    df2.to_excel(writer, 'Заказы')
    writer.save()

    df3 = pd.read_sql_query("SELECT * from TransactionsDB", conn)
    writer = pd.ExcelWriter(f"{savepass}/Transactions.xlsx")  # f"{savepass}/Result.xlsx"
    df3.to_excel(writer, 'Транзакции')
    writer.save()

    conn.close()

#

# passoffile = '/home/kira/PycharmProjects/pythonProject/data/Клиенты.xlsx'
# savepass = '/home/kira/PycharmProjects/pythonProject/data'
# form_custom_base(passoffile)
# mycount = service(passoffile)
# savexcl(savepass, passoffile)
# print(mycount[0], mycount[1])
