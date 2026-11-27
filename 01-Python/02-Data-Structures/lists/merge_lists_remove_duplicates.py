num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

#第一种方法强制转换数据类型
n = len(num_list2)
for i in range(n):
    num_list1.append(num_list2[i])
num_list = set(num_list1)
num_list = list(num_list)
print(num_list)


#第二种方法利用解包,组包操作
num_List = [*num_list1,*num_list2]  #num_List = num_list1 + num_list2直接加也可以
new_list = []
for i in num_List:
    if i not in new_list:
        new_list.append(i)
print(new_list)