def c(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
m=int(input())
n=int(input())
if c(m)==n and c(n)==m:
    print("Amicable")
else:
    print("Not Amicable")