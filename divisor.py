def solution(left,right):
    numbers = list(range(left,right+1))
    answer = 0
    for idx in numbers:
        cnt=0
        for i in range(1,idx+1):
            if idx%i ==0:
                cnt+=1
        if cnt%2==0:
            answer+=idx
        else:
            answer-=idx

    return answer

