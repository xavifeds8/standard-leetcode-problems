nums = list(map(int , input.split()))
if not len(nums):  print(0)
nums.sort()
i = 0
for j in range(len(nums)):
    if nums[i]!= nums[j]:
        i+=1
        nums[i] = nums[j]
nums = nums[:i+1]
print(nums)
max_count = 1
count = 1
for i in range(1 , len(nums)):
    if nums[i] == nums[i-1]+1:
        count +=1
    else:
        count = 1
    max_count = max(count , max_count)

print(max_count)