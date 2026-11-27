#元组是不可以进行增删改除的,如果要变用列表
#多用列表当中的函数
#在不知道个数时可以利用反向索引


stu_tuple = (
("S001","王林",85,92,78),
("S002","李慕婉",92,88,95),
("S003","曾牛",88,79,91),
)


print(f"学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
for s in stu_tuple:   # 当前的s已经是每一个学生的元组了
    total = s[2] + s[3] + s[4]
    # stu[2:5] 取出了 [85, 92, 78] 然后用 sum() 求和
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

chinese_scores = [s[2] for s in stu_tuple]
english_scores = [s[3] for s in stu_tuple]
math_score = [s[4] for s in stu_tuple]
chinese_scores.sort()
english_scores.sort()
math_score.sort()
print(f"""
语文最低分：{chinese_scores[0]},最高分：{chinese_scores[-1]},平均分:{sum(chinese_scores)/len(chinese_scores):.1f}""")
#或者使用min()
print("优秀学生有：")
for s in stu_tuple:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 80:
        print(f"{s[0]} \t {s[1]}")