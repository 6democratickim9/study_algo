# import math

# def solution(n, m):
#     answer = []
#     answer.append(math.gcd(n,m))
#     answer.append(math.lcm(n,m))
    
#     return answer

def solution(n,m):
    n1,m1=n,m
    answer=[]
    while m:
        n,m = m,n%m
    answer.append(n)
    answer.append(n1*m1//n)
    return answer
# 유클리드 호제법 이용해서 문제풀기
print(solution(2,5))