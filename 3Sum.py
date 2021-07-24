nums = [-1, 0, 1, 2, -1, -4]
# o(n**2) is to use 2 sums
nums.sort()
print(nums)
# [-4, -1, -1, 0, 1, 2]
n = len(nums)
for i in range(len(nums)):
    f, l = i+1 ,len(nums)-1
    while f<l: #target -nums[i]=nums[f]+nums[l]
        target = -nums[i] #4
        if nums[f]+nums[l] < target:
            f+=1
        elif nums[f]+nums[l] > target:
            l-=1
        else:
            print(nums[i] , nums[f] ,nums[l])
            break
