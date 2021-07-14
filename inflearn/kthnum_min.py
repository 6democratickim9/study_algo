import sys

def solution(array, commands):
    answer = []
    for roll in range(len(commands)):
        tmp=array[(commands[roll][0])-1:(commands[roll][1])]
        tmp.sort()
        answer.append(tmp[commands[roll][2]-1])

    return answer

# 인덱스 슬라이싱도 for문처럼 이전 숫자 인덱스까지만 들어감

