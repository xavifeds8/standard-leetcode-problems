"""xor of elements of subarray is m 
[4 , 2 , 2 , 6 , 4]
<---XR------> prefix xor
___________
<---><----->
  Y      k
XR = Y ^ k  --> Y = XR ^ k
count the number of y which 
satis fies the above equation 
O(nlog(n))
"""
k = 6
nums = [4 , 2, 2, 6 , 4]
freq = {}
xr = 0
cnt = 0
for i in range(len(nums)):
    xr = xr ^ nums[i]
    if xr == k: cnt+=1
    if xr^k in freq: cnt += freq[xr^k]
    freq[xr] = freq.get(xr,1)+1
print(cnt)



    
