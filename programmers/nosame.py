def solution(arr):
    answer = []
    answer.append(arr[0])
    i=0
    for i in range(len(arr)):
        if arr[i]!=int(answer[-1]):
            print(arr[i],answer[-1])
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))