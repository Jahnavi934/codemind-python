n=int(input())
d=list(map(int,input().split()))
c=[]
for i in d:
    if i%2==1:
        c.append(i)
for i in d:
    if i%2==0:
        c.append(i)
print(*c)