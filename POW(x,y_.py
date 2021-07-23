def pow(x , n):
    if n==0: return 1
    if n==-1: return 1/x
    sub = pow(x,n//2)
    if n%2:return sub*sub*x
    else: return sub*sub
x,y = map(float , input().split())
print(pow(x , y))