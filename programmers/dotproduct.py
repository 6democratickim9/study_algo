def solution(a, b):
    return sum(list(map(int,(a[i]*b[i] for i in range(len(a))))))

# def solution(a, b):

#     return sum([x*y for x, y in zip(a,b)])
# 리스트 a,b의 각 요소 x,y를 빼서 x*y를 곱한 리스트를 만들고 sum으로 모두 합쳐준다.