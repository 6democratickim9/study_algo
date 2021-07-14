def solution(numbers):
    tmp = 0
    answer = []
    length = len(numbers)
    for idx in range(len(numbers)):
        for index in range(len(numbers)):
                if idx!=index:
                    tmp = numbers[idx]+numbers[index]
                    answer.append(tmp)
    answer = list(set(answer))
    answer.sort()
    return answer