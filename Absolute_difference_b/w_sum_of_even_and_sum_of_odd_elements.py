n=int(input())
d=list(map(int,input().split()))
e=0
o=0
for i in d:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))