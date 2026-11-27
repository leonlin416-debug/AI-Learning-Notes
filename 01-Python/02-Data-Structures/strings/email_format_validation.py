mail = input("请输入邮箱：")
n = 0
# for i in mail:
#     if i == "@":
#         n += 1
# if n == 1 and "." in mail:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

#用内置函数
if mail.count("@") == 1 and mail.count(".") >= 1:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

