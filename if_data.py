# if False:
#     print("Hello World")
# else:
#     print("Hello Python")


# 获取当前的时间
import time

# print(time.time())
# print(time.localtime())

current_time = time.strftime("%Y-%m-%d", time.localtime())
if current_time == "2025-01-27":
    print("今天是2025-01-27")
else:
    print("今天不2025-01-27")
