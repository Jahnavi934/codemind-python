n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    if i%2==1:
        break
    s=s+i
print(s)