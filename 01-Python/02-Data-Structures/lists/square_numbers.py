square_list = []
for i in range(1,21):
    square_list.append(i**2)
print(square_list)

num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list = [i**2 for i in num_list if i % 2 == 0]   #列表推导式 快速构建新的列表
# for num in num_list:
#     if num % 2 == 0:
#         new_list.append(num**2)

print(new_list)