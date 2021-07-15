
def solution(arr1, arr2):
    answer = []
    
    for a in range(0,len(arr1)):
        tmp=[[]]
        for b in range(0,len(arr1[a])):
            tmp[0].append(arr1[a][b]+arr2[a][b])
        answer=answer+tmp
    return answer

# def solution(arr1, arr2):
#     answer = [[],[]]
#     for a in range(0,len(arr1)):
#         for b in range(0,len(arr1[a])):
#             answer[a].append(arr1[a][b]+arr2[a][b])
#     return answer
# 내 답안. 왜 틀린건지 집 가서 찾아보기

# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
# A,B 의 원소 ab에서 a,b 내의 c,d 를 더해서 zip한다.
#     return answer

print(solution([[1],[2]],[[3],[4]]))
print(solution([[1,2,3,4,2],[4,2,5,6,3]],[[1,2,3,3,4],[1,2,3,5,6]]))