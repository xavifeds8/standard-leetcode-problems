#maximum sub array sum
a = [-2 , -3 ,  4 , -1 , -2 , 1 , 5 ,-3]
sum = -1000
max_sum = 0
for i in range(len(a)):
    sum += a[i]
    if sum < 0:
        sum = 0
    if sum > max_sum:
        max_sum = sum
    print(sum)
print(max_sum)
