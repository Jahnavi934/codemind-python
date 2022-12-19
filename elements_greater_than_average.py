n=int(input())
d=list(map(int,input().split()))
s=sum(d)
c=0
avg=s//n
for i in d:
    if i>=avg:
        c+=1
print(c)
        