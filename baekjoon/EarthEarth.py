import sys
import itertools
N=int(sys.stdin.readline())
num=list(i for i in range(1,N+1))
answer=list(itertools.combinations_with_replacement(num,len(num)))
print(len(list(answer)))

print(list(itertools.combinations('ABCD',4)))