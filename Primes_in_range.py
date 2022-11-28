def prime(n):
    s=0
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s=1
            break
    if s==0:
        return True
    else:
        return False
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i):
        c+=1
print(c)
