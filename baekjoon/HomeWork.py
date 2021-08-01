import sys
input = sys.stdin.readline
N=int(input())
tmp=''
answer=list()
for _ in range(N):
    put=input()
    for i in range(len(put)):
        if put[i].isdigit()==True:
            tmp=tmp+put[i]
        elif isinstance(put,str)==True and len(tmp)>0:
            answer.append(int(tmp))
            tmp=''
        elif isinstance(put,str)==True and len(tmp)==0:
            continue
        
answer.sort()
for idx in answer:
    print(int(idx))

# 차례대로 읽어오면서 더해주고 다음 인덱스가 숫자가 아니면 answer에 더해준다

