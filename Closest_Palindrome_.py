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
        return False
n=int(input())
for i in range(n+1,999999):
    if p(i):
        a=i
        break
for i in range(n-1,0,-1):
    if p(i):
        b=i
        break
if a-n<n-b:
    print(a)
elif a-n==n-b:
    print(b,a)
else:
    print(b)