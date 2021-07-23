from typing import Counter


m , n = map(int , input().split())
count = 0
def gridPath(i , j):
    if i>m or j>n:
        return 0
    if i==m-1 and j==n-1:
        return 1
    return gridPath(i+1 , j) + gridPath(i , j+1)
print(gridPath(0 ,0))
