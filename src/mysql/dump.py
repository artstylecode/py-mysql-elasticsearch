import pymysql.cursors

connecntion = pymysql.connect(
                            host='127.0.0.1',user='root', 
                            password='000000', db='test', 
                            charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                            )
try:
    with connecntion.cursor() as cursor:
        sql = "insert into test (name) values(%s)"
        cursor.execute(sql,('test6'))
    connecntion.commit()
finally:
    connecntion.close()