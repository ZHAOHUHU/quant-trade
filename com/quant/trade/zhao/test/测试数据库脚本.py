import pymysql as sql
import pandas as pd

if __name__ == '__main__':
    # 创建连接
    db = sql.connect(host="localhost", user="root", password="74110", database="quant-trade", port=3307,
                     autocommit=True,autoclose)
    # c创建游标
    cur = db.cursor()
    insert_sql = 'INSERT into `tralling-stop` (code,high_price,low_price,name,price,count) VALUES (%s,%s,%s,%s,%s,%s)'
    array = ['sh0001', 12, 10, '中国平安', 11, 100]
    cur.execute(insert_sql, array)
    select_sql = "select * FROM `tralling-stop`"
    cur.execute(select_sql)
    df = pd.DataFrame(list(cur.fetchall()))
    print(df)
    cur.close()
