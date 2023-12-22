from typing import Set
import pymysql

def insert_data(email, password):
    db = pymysql.connect(host='127.0.0.1',
    user='root',
    password='1234', db='dbdb',
    charset='utf8')

    c = db.cursor()
    setdata = (email,password)
    c.execute("INSERT INTO user_tb VALUES (%5, %5)", setdata)
    db.commit()

def get_emailpassword(email, password):
    db = pymysql.connect(host='127.0.0.1',
    user='root',
    password='1234', db='dbdb',
    charset='utf8')

    c = db.cursor()
    setdata = (email,password)
    c.execute("SELECT +FROM user_tb WHERE email = %s AND password = %s", setdata)
    ret = c.ftechone()
    print(ret)