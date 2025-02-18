from redis import Redis

#  连接到 Redis 服务器
# (如果 Redis 服务器运行在本地， 并且使用默认端口 6379， 则可以省略 host 和 port 参数)
try:
    connect = Redis(host="127.0.0.1", port=6379)  #  连接 Redis
    # 如果设置了密码， 需要进行认证
    # connect.auth('your_password')

    #  测试连接
    connect.ping()
    print("Redis 连接成功！")

    #  进行一些 Redis 操作
    connect.set("name", "ankouyang")  # 设置键值对
    value = connect.get("name")  # 获取键值对
    print("name:", value)

except Exception as e:
    print(f"Redis 连接失败： {e}")  # 打印错误信息
