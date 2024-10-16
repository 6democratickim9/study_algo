# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = n + 1
#     정답 수의 2진수화의 1 갯수가 인풋 수의 2진수화의 1갯수가 같지 않은 경우 정답 수 1씩 증가
    while bin(answer)[2:].count("1") != bin(n)[2:].count("1"):
        answer += 1
    return answer