import mysql.connector

myDB = mysql.connector.connect(
    host='192.168.2.57',
    port='3306',
    user='www',
    passwd='xykj'
)

myCursor = myDB.cursor()

sql = 'select * from crm.operator_order_management where user_id=6003640;'
myCursor.execute(sql)

result = myCursor.fetchall()
print(type(result))

for i in result:
    print(type(i))
    print(i)

# myDB.commit()    # 数据表内容有更新，必须使用到该语句
