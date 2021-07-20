# 에라스토스테네스의 체 활용코드. 따라서 나도 잘 모르므로 주석 달아둠
def Primenum(n):
    a = [False,False] + [True]*(n-1)
    # 0,1은 치지 않으니 False, 2부터 n-1개까지(n개 사이에 있는 숫자이므로 n까지 치지 않음)배열을 하나 만든다
    primes=[]
    # 소수를 담을 리스트 생성

    for i in range(2,n+1):
        # 2부터 n까지 range 돈다
        if a[i]:
            # a[i]값이 참이면 예: a[2]값이 참이면--> 2는 True이므로 참
            primes.append(i)
            # primes 에 i값을 넣어준다
            for j in range(2*i, n+1, i):
                #  i에 2를 곱한 수부터 n+1까지 i만큼의 간격으로 돌아간다 예: i가 2면 2*2부터 n+1까지 2만큼 올라간다.
                #  n*1은 배수 당사자(?)이므로 2부터 해야 배수...
                a[j] = False
                # 그 값을 false로 바꿔줌
    return len(primes)
# 사람들은 똑똑하다...수포하지 말걸...그래도 수포한만큼 열심히 해야지ㅠㅠ

# def solution(n):
#     num=set(range(2,n+1))
#     # 2부터(1은 안치니까)n까지의 range를 설정
#     for i in range(2,n+1):
#         # 2부터 n+1까지 차례대로 돈다
#         if i in num:
#             # 선언한 range에 for문의 값이 있다면
#             num-=set(range(2*i,n+1,i))
#             #  2*i부터 n까지 i의 간격만큼 set을 만들어서 num 에서 제거한다(해당 값의 배수이기 때문)
#             print(num)
#     return len(num)
#     # 남은 값의 길이를 반환한다.

print(Primenum(10))

