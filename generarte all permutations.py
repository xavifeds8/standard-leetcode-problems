#using recursion
# def genPrem(string , rem):
#     if string == "":
#         print(rem)
#         return 
#     for i in range(len(string)):
#         genPrem(string[:i]+string[i+1:] , rem + string[i])
# genPrem("123" ,"")

#using backtracking

def genPermBack(lst , setIndex):
    if setIndex == len(lst)-1:
        print(lst)
        return
    for i in range(setIndex , len(lst)):
        lst[setIndex] , lst[i]  = lst[i] , lst[setIndex] 
        genPermBack(lst , setIndex+1)
        lst[setIndex] , lst[i]  = lst[i] , lst[setIndex] 
genPermBack([1 , 2 , 3 ,4 ,5] , 0)

