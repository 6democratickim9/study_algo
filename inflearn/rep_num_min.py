# 리스트로 입력 받음
# sum,round로 평균점수 구함
# map으로 sum에서 각 학생점수 뺌
# min점수 가진 index 호출

# 내용 소수점 올림

import sys
import math
sys.stdin = open("input.txt", "rt")

def minus(num):
    return abs(num-avg)
close=[]
N = int(sys.stdin.readline())
grade=list(map(int,sys.stdin.readline().split()))
avg=int(round(sum(grade)/N,0))
re=list(map(minus,grade))
for a in range(len(re)):
    if re[a]==min(re):
        close.append(grade[a])

print(avg,grade.index(max(close))+1)
# 0에 가까운 값을 가진 학생의 index를 return
