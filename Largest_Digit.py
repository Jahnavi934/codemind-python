n=int(input())
a=0
while n>0:
    r=n%10
    if r>a:
        a=r
    n=n//10
print(a)