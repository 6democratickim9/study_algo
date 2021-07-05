def solution(N, stages):
    answer = []
    current = len(stages)
    fail = [0] * (N+1)
    
    for i in range(1, N+1) :
        cnt = stages.count(i)
        try:
            fail[i] = cnt / current
            current -= cnt
        except:
            break

    for idx, _ in sorted(enumerate(fail[1:]), key = lambda x : x[1], reverse = True) :
        answer.append(idx+1)
    print(answer)
    return answer
solution(5,[2, 1, 2, 6, 2, 4, 3, 3])