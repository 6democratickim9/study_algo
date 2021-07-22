import sys
from math import gcd
input = sys.stdin.readline
T=input()
for re in range(int(T)):
    m,n=input().split()
    m=int(m)
    n=int(n)
    print(m * n // gcd(m, n))

