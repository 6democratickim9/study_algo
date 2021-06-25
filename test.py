def solution(param0):
    dic = {"BOOL": 1, "SHORT": 2, "FLOAT": 4, "INT": 8, "LONG": 16}
    tmp = answer = ''
    counts = temp = 0

    for idx, val in enumerate(param0):
        counts += dic[val]
        answer = answer+"#"*dic[val]
        if idx!=len(param0)-1:
            if dic.[val]+dic.values[idx+1]>8:
                temp = 8- param0.values[idx]+param0.values[idx+1]
                answer+='.'*temp
            if dic.values[idx]+dic.values[idx+1]<8:
                answer+='.......'

        if counts%8==0:
            answer=answer+","
        if counts >= 128:
            return "HALT"
            break

    print(answer)
    return answer


solution(["INT", "INT", "BOOL", "SHORT", "LONG"])
