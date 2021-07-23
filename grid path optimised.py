"""
10  6  3  1 
4  3  2  1
1  1  1  1
"""
def disp(m):
    print("___________________")
    for i in m:
        print(i)
    print("___________________")
m , n = map(int , input().split())
dp = [[0 for i in range(n+1)] for j in range(m+1)]
dp[m-1][n-1] = 1
disp(dp)
for i in range(m-1, -1 ,-1):
    for j in range(n-1, -1 , -1):
        if i==m-1 and j == n-1:
            continue
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        # dp[i][j] = -1
        disp(dp)

disp(dp)
