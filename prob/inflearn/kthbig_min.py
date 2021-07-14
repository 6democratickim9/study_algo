import sys
import itertools
n,k = (map(int,sys.stdin.readline().split()))
cards=(list(map(int,sys.stdin.readline().split())))
add=list(map(sum,itertools.combinations(cards,3)))
add.sort(reverse=True)
print(add[k-1])
