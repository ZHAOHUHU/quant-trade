# 移动止盈止损策略 赢损比自定义 默认1.5：1
import pymysql as sql
import pandas as pd
import requests as req

db = sql.connect(host="localhost", user="root", password="74110", database="quant-trade", port=3307,
                 autocommit=True)
sina_url = 'http://hq.sinajs.cn/list='


# 获取新浪财经的指定股票实时数据返回dateframe类型
#参考链接 https://www.jianshu.com/p/108b8110a98c
def real_time_stock_price(stock_array):
    url = sina_url + ",".join(str(i) for i in stock_array)
    reslut_json = req.get(url).text
    df = pd.DataFrame(reslut_json)
    print(df)


if __name__ == '__main__':
    real_time_stock_price(['sz002307', 'sh600928'])


# 增删改的sql
def sql_fun(sql, args_array):
    con = db.cursor()
    result = con.execute(sql, args_array)
    con.close()
    return result


# 查询的sql
def get_sql_fun(select_sql, args_array):
    con = db.cursor()
    con.execute(sql, args_array)
    df = pd.DataFrame(list(con.fetchall()))
    con.close()
    return df
