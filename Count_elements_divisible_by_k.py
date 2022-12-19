m,n=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if i%n==0:
        c+=1
print(c)