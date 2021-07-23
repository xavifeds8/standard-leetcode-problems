arr1 = [1, 5, 9, 10, 15, 20,45,75,234,745]
arr2 = [2, 3, 8, 13,25]
fptr = len(arr1)-1
sptr= 0

while sptr<len(arr2) and fptr >=0:
    if arr1[fptr] > arr2[sptr]:
        arr1[fptr] , arr2[sptr] = arr2[sptr] , arr1[fptr]
        fptr -=1
        sptr+=1
    else:
        break
    print(arr1 , arr2)
print(sorted(arr1) , sorted(arr2))



