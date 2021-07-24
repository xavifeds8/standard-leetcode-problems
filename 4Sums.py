nums = [1,0,-1,0,-2,2]
nums.sort()
target = 0
lst = []
for i in range(len(nums)):
    for j in range(i+1 ,len(nums)):
        f , l = j+1  , len(nums)-1
        while f<l:
            targetTemp = target-nums[i]-nums[j]
            if nums[f]+nums[l] > targetTemp:
                l-=1
            elif nums[f]+nums[l] < targetTemp:
                f+=1
            else:
                osf = [nums[i] , nums[j] , nums[f] , nums[l]]
                lst.append(osf)
                while f<l and nums[f] == osf[2]: f+=1
                
                while f<l and nums[l] == osf[3]: l-=1
print(lst)