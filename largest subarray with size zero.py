#good question 
#O(n**2) generate all the sub arrays

#O(n) using the prefix sum property
nums = 15,-2,2,-8,1,7,10,23
max_len = 0
lst = []
d = {}
prefix_sum = 0
arrlen = 0
for i in range(len(nums)):
    prefix_sum = prefix_sum + nums[i]
    if prefix_sum == 0:
        max_len = i+1
        lst.append(nums[:i+1])
    elif prefix_sum not in d:
        d[prefix_sum] = i
    else:
        arrlen = i - d[prefix_sum]
        lst.append(nums[d[prefix_sum]+1:i+1])
    max_len = max(arrlen , max_len)
print(max_len)
print(lst)
