code = {"admin":"666888",
        "zhangsan":"123456",
        "wangge":"888666"}  #密码如果直接输入数字会认定为整型 所以应该用字符串
while True:
    name = input("请输入用户名:")
    mima = input("请输入密码:")
    if name == "" or mima == "":    # 输入字符串为空时的比较
        print("用户名和密码不能为空！")
        print("*" * 30)
        continue    #直接跳出进行下一次
    elif name in code:
        if code[name] == mima:
            print(f"登陆成功，欢迎{name}进入")
            print("*" * 30)
            break
        print("用户名或密码错误，请重新输入！")
        print("*"*30)
    else:
        print("用户名或密码错误，请重新输入！")
        print("*"*30)
