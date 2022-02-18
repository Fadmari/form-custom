import pandas as pd
import sqlite3

def get_customid (passofbase, onerow):
    passdb = passofbase[:passofbase.rfind('/')] + '/mybase/customDB.sqlite'
    # passdb = 'customDB.sqlite' #/mybase/
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT userid FROM customDB WHERE instr(customDB.tel, ?) !=0 AND instr(customDB.client, ?) "
                       "!=0", (onerow[3], onerow[2][1:-1]))
        customid = cursor.fetchone()[0]
        onerow.append(customid)
    except:
        customid = ''
        onerow.append(customid)
    return onerow

# passoffile = '/home/kira/PycharmProjects/pythonProject/data/Orders.xlsx'
# data = ['2022-9753', 'A 312283', ' Андрей ', '+7-906-567-77-71', 0.0, '₽', '0.00 ₽', 'Нал', 0.0, '₽', '0.00 ₽', '', '', '308999']
#
# data2 = get_customid(passoffile, data)
# print(data2)