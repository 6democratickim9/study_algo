import sys
input = sys.stdin.readline
n,m=(input().split())
cnt=0
castle = [input() for row in range(int(n))]
for idx in castle:
    if 'X' not in idx:
        cnt+=1
print(cnt)