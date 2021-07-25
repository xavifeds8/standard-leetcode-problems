#O(n^2)
s = "abcabcbb"
#generate all the substrings
# for i in range(len(s)):
#     for j in range(i , len(s)):
#         print(s[i:j+1])
        #check if there are reapeating charaters

#O(2n) using a set 

s = "abcabcbb"
visited = set()
j = 0
cnt = 0
max_cnt = 0
for i in range(len(s)):
    if s[i] not in visited:
        visited.add(s[i])
    else:
        cnt = i-j+1
        max_cnt = max(cnt , max_cnt)
        cnt = 0
        while s[i] in visited: 
            visited.remove(s[j])
            j+=1
print(max_cnt)

