
# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    # x를 구하는 공식
    # x + (x+1) + (x+2) + ... + (x + (num - 1)) = num * x + num(num - 1)/2
    # 등차수열의 합 공식으로 계산
    x = (total - (num * (num - 1)) // 2) // num
    
    # 연속된 num개의 숫자를 구함
    return [x + i for i in range(num)]
