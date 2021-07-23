#normal sort
#counting sort
#dutch national flag algorithm 
lst = [2,0,2,1,1,2]

low , high , mid = 0 , len(lst)-1 , 0

while mid< high:
    if lst[mid] == 0: 
        lst[mid] , lst[low] = lst[low] , lst[mid]
        low+=1
        mid+=1
    elif lst[mid] == 1:
        mid+=1
    elif lst[mid] == 2:
        lst[mid] , lst[high] = lst[high] , lst[mid]
        high-=1
print(lst)