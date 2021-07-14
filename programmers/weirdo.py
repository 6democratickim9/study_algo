def solution(s):
    tmp = s.split(' ')
    answer=''
    for id1,val1 in enumerate(tmp):
        for id2,val2 in enumerate(val1):
            if id2%2==0 or id2 ==0:
                answer+=tmp[id1][id2].upper()             
            else:
                answer+=tmp[id1][id2].lower()

        answer+=' '
    return answer[:-1]
