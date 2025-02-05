# number = 1
# while number <= 3:
#     print(number)
#     number += 1


# number = 10
# while number >= 1:
#     number -= 1
#     if number == 5:
#         # break
#         continue
#     print(number)

# 列表
# list = []
# number = 1
# while number < 5:
#     list.append(number)
#     number += 1

# print(list)

# list1 = [1, 2, 3, 4, 5]
# while list1:
#     print(list1.pop())
#     print(list1)

# 遍历一个对象中的所有元素
# 遍历set对象
# my_set = {"a", "b", "c", "d", "e"}
# while my_set:
#     print(my_set.pop())
#     print(my_set)

# 遍历元组
# color = ("r", "g", "b", "g", "b", "g")
# while color:
#     # print(color.pop())
#     # 删除元组的元素
#     # color.pop()
#     print(color)

# for i in range(1, 5):
#     print(i)

# 遍历序列
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# 遍历字典
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key in my_dict:
#     print(key, my_dict[key])
# for key, value in my_dict.items():
#     print(key, value)
# for value in my_dict.values():
#     print(value)

# 遍历字典，并添加序号
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for i in enumerate(my_dict.items()):
    print(i)
