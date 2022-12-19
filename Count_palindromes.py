def p(n):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if t==s:
        return True
    else:
        False
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if p(i):
        c+=1
print(c)