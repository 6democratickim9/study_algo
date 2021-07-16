def solution(a, b):
    if a>b:
        a,b=b,a
    return sum(list(i for i in range(a,b+1)))
# def adder(a, b):
#     # 함수를 완성하세요
#     if a > b: a, b = b, a
#     return sum(range(a,b+1))
#     # range를 돌면서 바로 sum이 가능하다는 것을 첨 알았다...ㅎ