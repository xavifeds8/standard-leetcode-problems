lst = [[1,1],[1,6],[8,22],[15,18]]
i = 0
while i<len(lst)-1:
    val = max(lst[i][1] , lst[i+1][1])
    if lst[i][1] >= lst[i+1][0]:
        lst[i+1] = [lst[i][0] ,val]
        lst.pop(i)
    i+=1
print(lst)