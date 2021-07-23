matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def disp(m):
    print("++++++++++")
    for i in m:
        print(i)
    print("++++++++++")
disp(matrix)
"""
1 0 1
1 0 1 
1 1 1

"""
isColZero = False
for i in range(len(matrix)):
    if matrix[i][0] == 0:
        isColZero = True
        continue
    for j in range(1 , len(matrix[0])):
        if matrix[i][j] ==0:
            matrix[i][0] = 0
            matrix[0][j] = 0
disp(matrix)
for i in range(len(matrix)-1  , -1 , -1):
    for j in range(len(matrix[0])-1 , 0 , -1):
        if matrix[i][0] == 0 or matrix[0][j] ==0:
            matrix[i][j] =0
    if isColZero==True:
        matrix[i][0]  = 0
disp(matrix)


        