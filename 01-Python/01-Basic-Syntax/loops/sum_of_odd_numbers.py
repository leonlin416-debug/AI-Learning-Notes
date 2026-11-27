sum1 = 0
for i in range(1,100,2) :
    sum1 += i
print(sum1)
sum2 = 0
for i in range(100,500) :
    if i % 3 == 0:
        sum2 += i
print(sum2)