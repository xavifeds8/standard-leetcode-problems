# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def disp(m):
    print("+++++++++++++++++++")
    for i in m:
        print(i)
    print("+++++++++++++++++++")
for i in range(len(matrix)):
    for j in range(i ,len(matrix)):
        matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
for i in range(len(matrix)):
    l= 0
    r = len(matrix)-1
    while l<r:
        matrix[i][l] , matrix[i][r] = matrix[i][r] , matrix[i][l]
        l+=1
        r-=1
disp(matrix)