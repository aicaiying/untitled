import pymysql

def connDb():
    #我们要想连接数据库，需要知道数据库的哪些信息
    #ip地址，端口号，用户名和密码
    conn=pymysql.Connect( host='127.0.0.1', user='root', password="root",
                 database="pirate", port=3306,charset='utf8')
    #查询hd_user表中所有的数据并且倒序打印
    sql='select * from hd_user order by id desc'
    #要想在数据库中执行这条语句，需要获取数据库的游标（光标）
    curs=conn.cursor()
    curs.execute(sql)
    #想获取数据库中最新的数据，那么就要把数据库所有数据倒序排序，然后用fetchone（）获取第一条数据
    result=curs.fetchone()
    #想获得所有的查询结果，fetchall()
    return result

if __name__ == '__main__':

    print(connDb())
