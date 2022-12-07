n=int(input())
arr=list(map(int,input().split()))
v=set(arr)
lst=[i for i in v if i%2!=0]
print(len(lst))