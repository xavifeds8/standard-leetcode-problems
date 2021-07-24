def MergeSort(a , l , r):
    if l>=r:
        return 
    mid = (l+r)//2
    MergeSort(a , l , mid)
    MergeSort(a , mid+1 , r)
    # a[l:r] = sorted(a[l:r])
    print(a[l:r])
a= [1,5,2,35,2,62,34]
print(MergeSort(a , 0 , len(a)))