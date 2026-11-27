str = input("请输入字符串")
n = len(str)
numa = 0
numk = 0
for i in range(n):
    if str[i] == "a" :
        numa += 1
    elif str[i] == "k" :
        numk += 1
print(f"a的个数为：{numa},k的个数为{numk}")