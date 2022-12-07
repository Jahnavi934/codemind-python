n=int(input())
arr=list(map(int,input().split()))
d=[]
f=[]
for i in range(len(arr)//2):
    d.append(arr[i])
for i in range(len(arr)//2,len(arr)):
    f.append(arr[i])
print(sum(d))
print(sum(f))