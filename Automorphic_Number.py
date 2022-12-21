import math
n=int(input())
a=int(math.log10(n)+1)
b=(n*n)%(10**a)
if b==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")