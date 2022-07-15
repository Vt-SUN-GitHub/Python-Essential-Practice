import pymysql

#数据库连接
conn = pymysql.connect(host='localhost',user='root',password='123',charset='utf8',database='python-essential-practice',port=3306,autocommit=True)

sql = 'select * from userInfo'

#使用cursor()方法创建一个cursor游标对象
cursor = conn.cursor()

cursor.execute("select version()")
data = cursor.fetchone()
print(data)

insertSql = 'insert into userInfo(username, password) values(%s, %s)'
cursor.execute(insertSql, ['ma','siYuan'])

result = cursor.execute(sql)
resultSet = cursor.fetchall()
print(resultSet)

cursor.close()
conn.close()



