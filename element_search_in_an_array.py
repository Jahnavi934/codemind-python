n=int(input())
d=list(map(int,input().split()))
m=int(input())
for i in d:
    if m==i:
        print("True")
        break
else:
    print("False")