nums = list(map(int , input().split()))
# m1 is to find all the permutations and seach for the particular permutation and return the next element 
"""
1 3 5 2 6 -----> 1 3 5 6 2
1 3 5 2 1 -----> 1 5 1 2 3
1 3 15 8 1 -----> 1 8 1 3 15
step 1:- from the end check if arr[i] < arr[i+1] index = i
step 2:- from the end check if arr[i] > arr[m]
step 3:- swap arr[i], arr[m] 
step 4:- sort from index i
"""
for i in range(len(nums)-2 , -1 , -1):
    if nums[i] < nums[i+1]:
        index = i
        break
for i in range(len(nums)-1 , -1 , -1):
    if nums[i] > nums[index]:
        nums[i] , nums[index] = nums[index] , nums[i]
        break
print(nums)
print(nums[:index+1] + nums[:index:-1])
# [1 ,2 ,62,2 ,63 ,1]