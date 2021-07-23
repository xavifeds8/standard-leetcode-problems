#moore's voting algorithm
# 1 1 1 1 1 2 3 4 5 6 3 3 2
# 1 2 3 4 5 4 3 2 1 0 1 (majority is == 3)
"""
this algorithm only guarantee's whether a number can be part of a solution 
it cannot confirm it"""
cnt = 0
nums = list(map(int , input().split()))
for i in nums:
    if cnt == 0:
        element = i
    if element == i: cnt+=1
    else: cnt-=1
print(element)
 