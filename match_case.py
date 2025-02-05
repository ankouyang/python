# 获取当前的时间
import time

current_time = time.strftime("%Y-%m-%d", time.localtime())

match current_time:
    case "2025-01-27":
        print("今天是2025-01-27")
    case _:
        print("今天不2025-01-27")
