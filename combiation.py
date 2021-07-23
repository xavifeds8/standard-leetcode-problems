"""
n C r = n! /((n-1)! * r!)
nCr = n-1 C r-1 + n-1 C r
"""
def CombRecursion(n , r):
    if n==r or r ==0:
        return 1
    return CombRecursion(n-1 , r-1) + CombRecursion(n-1 , r)
print(CombRecursion(5 , 2))

#using dynamic programming 
"""
n = rows
r = cols
"""
def disp(m):
    print("_______________________________________")
    for i in m:
        print(i)
    print("_______________________________________")

def bottom(n , k):
    dp  = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1 ,n+1):
        for j in range(min(i,k)+1):
            if j==0 or i==j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp
disp(bottom(10,10))