# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse = True)
    for idx in range(len(A)):
        answer += A[idx] * B[idx]

    return answer

# 곱셈에서는 작은 수가 큰 수를 줄이는 효과가 있음