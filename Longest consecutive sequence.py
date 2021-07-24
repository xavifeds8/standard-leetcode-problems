nums = [0,3,7,2,5,8,4,6,0,1]
nums.sort()
max_val =0
cnt =  1
# [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(nums)-1):
    if nums[i] + 1 == nums[i+1]: 
        cnt +=1
        max_val =  max(max_val , cnt)
    else: 
        cnt= 1
print(max_val)
print(nums)