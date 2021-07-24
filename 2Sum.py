lst = list(map(int ,input().split()))
#n**2---> nlogn -->n , n
target = 9
s = {}
for i in range(len(lst)):
    if -(lst[i]-target) in s:
        print(s[-(lst[i]-target)] , i)
        break
    else:
        s[lst[i]] = i
