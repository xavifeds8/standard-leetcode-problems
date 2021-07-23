#pascals using combination formula
pascals = []
def CombRecursion(n , r):
    if n==r or r ==0:
        return 1
    return CombRecursion(n-1 , r-1) + CombRecursion(n-1 , r)
n = 10
val = []
for i in range(n):
    for j in range(0 , i+1):
        val.append(CombRecursion(i , j))
    pascals.append(val)
    val = []
print(pascals)