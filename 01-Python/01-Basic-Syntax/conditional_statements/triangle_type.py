a = int(input("请输入三角形的第一条边"))
b = int(input("请输入三角形的第二条边"))
c = int(input("请输入三角形的第三条边"))
if a + b <= c or b + c <= a or c + a <= b:
    print("不能构成三角形")
elif b == a or b == c or c == a:
    print("三角形为等腰三角形")
elif a == b == c:
    print("三角形为等边三角形")
else:
    print("三角形为普通三角形")
