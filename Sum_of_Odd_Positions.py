n=int(input())
d=list(map(int,input().split()))
s=0
for i in range(n):
    if i%2:
        s+=d[i]
print(s)