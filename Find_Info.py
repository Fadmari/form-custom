import pandas as pd
import sqlite3


def find_transaction(bdpass, number):
    passdb = f"{bdpass}/customDB.sqlite"
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("SELECT id_deal, Custom, tel, " +
                   "(SELECT mail FROM customDB WHERE instr(customDB.tel, OrderDB.tel) != 0) as mail, " +
                   "order_cost, payment_type FROM OrderDB WHERE instr(num_of_transaction, ?) !=0", (number,))
    df = cursor.fetchall()
    conn.close()
    return df

def find_custom_tel(bdpass, number):
    passdb = f"{bdpass}/customDB.sqlite"
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()
    newTel = number.zfill(11)
    newTel = ('+7-{}-{}-{}-{}'.format(newTel[1:4], newTel[4:7], newTel[7:9], newTel[9:11]))

    cursor.execute("SELECT client, gender, tel, mail, client_type " +
                   "FROM customDB WHERE instr(customDB.tel, ?) != 0",(newTel,))
    df = cursor.fetchall()
    conn.close()
    return df

def find_custom_name(bdpass, name):
    passdb = f"{bdpass}/customDB.sqlite"
    conn = sqlite3.connect(passdb)
    cursor = conn.cursor()

    cursor.execute("SELECT client, gender, tel, mail, client_type " +
                   "FROM customDB WHERE instr(customDB.client, ?) != 0", (name,))
    df = cursor.fetchall()
    conn.close()
    return df
#
# bdpass = '/home/kira/PycharmProjects/pythonProject/data/mybase'
# number = '308956'
#
# # res = find_transaction(bdpass, number)
# # print(res)
# res = find_transaction(bdpass, number)
# print(res)
