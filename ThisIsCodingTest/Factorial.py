# 반복적으로 구현한 n!
def factorial_iterative(n):
    result=1
    for a in range(1,n+1):
        result+=a
    return result

# 재귀적으로 구현한 n!
# 점화식이라고도 표현
def factorial_recursive(n):
    if n<=1:
        # n이 1 이하인 경우 1을 반환
        return 1
        # n!=n*(n-1)!를 그대로 코드로 작성하기
    return n* factorial_recursive(n-1)