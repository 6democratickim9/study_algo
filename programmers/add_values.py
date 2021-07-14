def solution(n):
    answer=0
    for a in range(len(str(n))):
        answer+=int(str(n)[a])
    return answer
print(solution(123))