n=int(input())
arr=list(map(int,input().split()))
b=int(input())
d=[]
for i in range(arr.index(b)+1):
    d.append(arr[i])
print(sum(d))
    