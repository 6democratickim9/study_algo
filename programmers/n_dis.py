def solution(x, n):
    return list(i*x for i in range(1,n+1))
    
print(solution(2,5))