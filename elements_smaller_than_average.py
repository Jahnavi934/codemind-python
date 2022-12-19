n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if i<=sum(d)//n:
        c+=1
print(c)
    