matrix = [[1]]
target = int(input("enter the number"))
m = len(matrix[0])
l = 0
h = len(matrix)*len(matrix[0])-1
val = False
while l<=h:
    mid = (l+h)//2
    if matrix[mid//m][mid%m] == target:
        val = True
        break
    elif  matrix[mid//m][mid%m] < target:
        l = mid+1
    else:
        h = mid-1
print(val)

    