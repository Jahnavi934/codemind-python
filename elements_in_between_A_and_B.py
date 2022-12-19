n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in d:
    if i>=a and i<=b:
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)
        