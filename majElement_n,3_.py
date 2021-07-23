nums = [3,2,3 ,3 ,3 ,3, 3, 2 , 2,2 ,2 ,2 ,2]
num1 = -1 
num2 = -1
cnt1 = 0
cnt2 = 0
for i in nums:
    if i == num1:
        cnt1+=1
    elif i==num2:
        cnt2 +=1
    if cnt1 ==0:
        num1 = i
        cnt1 = 1
    elif cnt2 ==0:
        num2 = i
        cnt2 = 1
    else:
        cnt1-=1
        cnt2-=1
print(num1 , num2)