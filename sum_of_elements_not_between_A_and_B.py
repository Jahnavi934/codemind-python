n=int(input())
d=list(map(int,input().split()))
b,c=map(int,input().split())
a=[]
for i in d:
    if i<b:
        a.append(i)
    if i>c:
        a.append(i)
print(sum(a))