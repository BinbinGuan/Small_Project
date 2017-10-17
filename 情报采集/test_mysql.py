# -*- coding:utf-8 -*-
import MySQLdb
conn = MySQLdb.Connect(
                   host = '120.27.101.31',
                   port = 3306,  #注意端口号为数字类型，其余都为字符串
                   user = 'root',
                   passwd = '******',
                   db = 'baijiahao',
                   charset = 'utf8'
                       )

cur = conn.cursor()
f = open("/home/xuna/桌面/res/时光，影视.txt",'r')

for line in f:
    if line !="\n":
        st = line.split("_&_")

        #print line.split("_&_")[1]

        #(id, title_str, max_num, price, remark, use_day, factory)

        id = "20171017"
        title_str = st[0]
        print title_str
        max_num = st[2]
        price = st[1]
        remark = "http://py.shiguangka.com/"
        use_day = ""
        factory = ""


        sql_insert = "insert into kameng values(%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql_insert,(id, title_str, max_num, price, remark, use_day, factory))


cur.close()
conn.commit()
conn.close()
