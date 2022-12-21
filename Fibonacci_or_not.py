n=int(input())
a=0
b=1
c=a+b
for i in range(0,n):
    if n==c:
        print("True")
        break
    a=b
    b=c
    c=a+b
else:
    print("False")