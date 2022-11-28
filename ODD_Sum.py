n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    if i%2:
        s+=i
print(s)