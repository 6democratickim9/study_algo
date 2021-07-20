import time
start=time.time()
import sys
sys.stdin = open("input.txt", "rt")
n,m=map(int,input().split())
cnt=[0]*(n+m+3)
# cnt는 0부터 시작하기땜에 n+m만큼의 리스트 길이가 있으려면 0,1과 n+m만큼까지 생각해서 3을 더해줘야됨(n,m의 최대값은 n+m이기때문)
max=-2147000000
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
# 차례대로 돌아가면서 각 번호가 나올때의 값을 cnt에 더해줌
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
# n+m만큼 돌려면 1을 더해줘야하므로 1을 더해주고
# max에 저장된 값보다 cnt[i]가크면 max에 해당 값을 저장한다 
for i in range(n+m+1):
    if cnt[i]==max:
        print(i,end=' ')
# cnt인덱스 길이만큼 돌면서 만약 max 값(cnt의 최대값)만큼의 값을 가진 인덱스가 있다면 해당 값을 출력한다. 
print("time: ",time.time()-start)