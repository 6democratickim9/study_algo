def solution(n):
    answer = []
    for a in range(len(str(n))):
        answer.append(int(str(n)[a]))
    answer.reverse()
    return answer

print(solution(12345))

#def digit_reverse(n):
#    return list(map(int, reversed(str(n))))
# n을 str으로 바꾼 후에 뒤집고, int로 만들어 list 에 매핑 