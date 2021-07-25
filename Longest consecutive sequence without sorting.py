#o(n) space 
nums = [100,4,200,1,3,2]
max_len = 1
for i in range(len(nums)):
    if nums[i]-1 not in nums:
        mlen = 1
        while nums[i]+mlen in nums:
            mlen+=1
        max_len = max(max_len , mlen)
print(max_len)