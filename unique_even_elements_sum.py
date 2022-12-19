n=int(input())
d=list(map(int,input().split()))
c=[]
for i in d:
    if i not in c:
        if i%2==0:
            c.append(i)
print(sum(c))