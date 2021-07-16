def solution(arr):
    answer = []
    for a in range(len(arr)):
        tmp = arr[0]
        answer.append(tmp)
        if len(arr)==arr.count(tmp):
            return answer
        for _ in range(arr.count(tmp)):
            if arr[0] != tmp :
                break
            (arr.pop(arr.index(tmp)))