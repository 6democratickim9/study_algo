def solution(n):
    answer = []
    for idx in range(1,n+1):
        if n%idx==0:
            answer.append(idx)
            
    return sum(answer)

print(solution(12))

# def sumDivisor(num):
#     return sum(list(filter(lambda i: not num % i, range(1, num + 1))))
#     # 필터를 거친 리스트를 sum 으로 반환한다
#     # 필터는 람다의 i가 1,num+1 까지 돌면서 num%1가 True가 아닌 것을 거른다.