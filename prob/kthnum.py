# def solution(array, commands):
#     answer = []
#     for roll in range(len(commands)):
#         tmp=array[(commands[roll][0])-1:(commands[roll][1])]
#         tmp.sort()
#         answer.append(tmp[commands[roll][2]-1])

#     return answer
# 여기까지가 내 풀이!

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 인덱스 슬라이싱도 for문처럼 이전 숫자 인덱스까지만 들어감

