def p(n):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if t==s:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    print(p(int(input())))