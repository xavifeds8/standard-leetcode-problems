nums = [0,1,1,1,2,2,3,3,4] #tricky concept
i=0 #points at the next not common element
for j in range(len(nums)):
    if(nums[i]!=nums[j]):
        i+=1
        nums[i]=nums[j]
print(nums[:i+1])