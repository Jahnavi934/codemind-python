n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    while i>0:
        r=i%10
        s+=r
        i=i//10
print(s)