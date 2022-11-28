n=int(input())
d=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        e+=d[i]
    else:
        o+=d[i]
print(abs(e-o))