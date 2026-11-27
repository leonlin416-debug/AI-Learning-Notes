nums = []
for i in range(10):
    n = float(input("请输入数字"))
    nums.append(n)
nums.sort()
print(f"最小值为{nums[0]},最大值为{nums[9]}")
print(f"最小值为{min(nums)},最大值为{max(nums)}")
print(f"平均值为：{sum(nums)/len(nums)}")
print(nums)