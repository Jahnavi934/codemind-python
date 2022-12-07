n=int(input())
arr=list(map(int,input().split()))
d=[]
flag=0
g=[]
for i in arr:
    if i not in g:
        g.append(i)
for i in g:
    h=arr.count(i)
    d.append(i)
    d.append(h)
print(*d)
      