def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
m=int(input())
c=0
for i in d:
    if m<=i:
        if prime(i):
            c+=1
print(c)
        