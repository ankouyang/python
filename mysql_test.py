import pymysql

# 打开数据库连接
db = pymysql.connect(
    host="xxxxxx",
    user="root",
    password="xxxxx",
    database="xxxxx ",
    port=60300,
)
with db:
    with db.cursor() as cursor:
        # 执行SQL语句
        cursor.execute("SELECT * FROM t_user WHERE `name` = 'yangke'")
        # 获取所有记录列表
        results = cursor.fetchone()
        # for row in results:
        #     print(row)
        print(results)
