n=int(input())
d=list(map(int,input().split()))
for i in range(n-1):
    if d[i]>d[i+1]:
        continue
    else:
        print("no")
        break
else:
    print("yes")