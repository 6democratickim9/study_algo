
def solution(answers):
    gvup1 = [1, 2, 3, 4, 5]
    gvup2 = [2, 1, 2, 3, 2, 4, 2, 5]
    gvup3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a=b=c=0
    tmp_answer = []
    answer =[]
    for index,value in enumerate(answers):
            if value == gvup1[index%5]:
                a+=1
            if value == gvup2[index%8]:
                b+=1
            if value == gvup3[index%10]:
                c+=1

    tmp_answer.append(a)
    tmp_answer.append(b)
    tmp_answer.append(c)

    for idx in range(len(tmp_answer)):
        if tmp_answer[idx]==max(tmp_answer):
            answer.append(idx+1)
        else:
            pass

    return answer

