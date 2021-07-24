import sys
input=sys.stdin.readline
A,B=input().split()
answer=[]
for a in range(0,int(A)):
    tmp=input().split()
    answer.append(min(tmp))
print(max(answer))

#답안은 하단에
# n,m=map(int,input().split())
# result=0
# for i in range(n):
#     data = list(map(int,input().split()))
#     min_value=min(data)
#     result=max(result,min_value)
# print(result)
# min()함수를 이용하는 답안 예시
