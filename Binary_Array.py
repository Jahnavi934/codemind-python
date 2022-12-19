n=int(input())
d=list(map(int,input().split()))
for i in d:
    if i!=1 and i!=0:
        print("False")
        break
else:
    print("True")
    