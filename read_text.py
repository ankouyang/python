import pprint

with open("./data/demo.txt", encoding="utf-8", errors="ignore") as f:
    text = f.readlines()
    pprint.pprint(text)

# 统计全部行数
# print(len(text))

# 输出每一行
# for line in text:
#     print(line)

# 统计空行行数
# print(text.count("\n"))

# 统计非空行行数
# print(len(text) - text.count("\n"))

# print(len(set(text)) - 1)
# print(len(set(text)))

# 统计单词 I 出现的次数
# print(str(text).split(" ").count("I"))


# 统计单词you出现的次数

# print(int(str(text).split(" ").count("you") + int(str(text).split(" ").count("You"))))


# 读取csv文件
# with open("./data/excel.csv", encoding="utf-8", errors="ignore") as f:
#     text = f.readlines()
#     pprint.pprint(text)

# # 指定存放通讯录的文件
# from tinydb import TinyDB

# # 使用TinyDB存储数据
# db = TinyDB("data/db.json")

# # 插入数据 但是我需要插入json 我需要将text进行分割
# # 通过循环将text进行分割,并转化成一个list中的 {key:value} 形式
# new_text_list = []
# for line in text:
#     line = line.strip().split(",")
#     # 姓名,年龄,职业
#     new_text_list.append({"name": line[0], "age": line[1], "job": line[2]})


# # 插入数据
# db.insert_multiple(new_text_list)


# # 根据姓名查电话
# from tinydb import Query

# friend = Query()
# print(db.search(friend.age == "22"))

# print(db.all())
