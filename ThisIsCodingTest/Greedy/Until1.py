#import sys
#input=sys.stdin.readline
#N,K=map(int,input().split())
#cnt=0
#while N>1:
#    if N%K!=0:
#        N-=1
#        cnt+=1
#    else:
#        N=int(N/K)
#        cnt+=1
#print(cnt)
#해답
n,k=map(int,input().split())
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n = target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)