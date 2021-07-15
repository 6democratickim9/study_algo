def solution(x):
    answer=0
    # for a in range(len(str(x))):
    #     answer+=int(str(x)[a])
    # answer=list(map(int,(str(x)[i] for i in range(len(str(x))))))
    answer=sum(list(map(int,(str(x)[i] for i in range(len(str(x)))))))
    if x%answer==0:
        return True
    else:
        answer=False



print(solution(10))
print(solution(12))
print(solution(13))