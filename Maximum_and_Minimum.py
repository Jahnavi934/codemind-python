n=int(input())
arr=list(map(int,input().split()))
d=[]
flag=0
for i in range(len(arr)):
    if (arr.count(arr[i])==arr[i]):
        if arr[i] not in d:
            d.append(arr[i])
            flag=1
if flag==1:
    print(min(d),max(d))
else:
    print("-1")