# import sys
# i = sys.stdin.readline
# T=int(i())
# for a in range(T):
#     n,m=map(int,i().split())
#     print(int(str(n**m)[-1:]))
# 여기까진 내 답
# 아무래도 형변환하는 과정에서 시간이 오래걸린듯ㅠㅠ

t = int(input())
# input으로 t 값을 받는다(int형임)
for _ in range(t):
    a, b = map(int,input().split())
    # a,b에 각각 int형으로 값을 받는다
    c = 1
    for __ in range(b):
        # 제곱하는 횟수 안에서 돌면서
        # c에 c와 a를 곱한 값에 10을 나눈 나머지값을 저장한다
        c = (c*a)%10
    if c == 0: print(c+10)
    else: print(c)