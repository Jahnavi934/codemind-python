n=int(input())
arr=list(map(int,input().split()))
if len(arr)%2==0:
    print(*arr)
else:
    print(*arr,end=" ")
    print("0",end=" ")