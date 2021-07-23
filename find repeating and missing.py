lst = [0]*(len(nums)+1)
print(lst)
for i in range(1 , len(lst)):
    lst[nums[i-1]] +=1

for i in range(len(lst)):
    if lst[i] == 2:
        rep = i
    if lst[i] == 0:
        rem = i
print([rep , rem])

# method 2
"""
S = (sum(natural) - sum(lst))
X-Y = S
X^2 - Y^2 = S^2

(X+Y)*S = S^2

(X+Y) = S

X = S
"""
