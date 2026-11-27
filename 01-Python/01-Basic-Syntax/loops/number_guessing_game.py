import random

n = random.randint(1, 101)# 随机生成整数
while True:
    m = int(input("请输入1-100之间的一个整数："))
    if 1<= m <= 100 :
        if m < n:
            print("猜小了")
        elif m > n:
            print("猜大了")
        elif m == n:
            print("猜对了！")
            break
    else:
        print("数值范围有误")


