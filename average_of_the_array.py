n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    s+=i
print('%.2f'%(s/n))