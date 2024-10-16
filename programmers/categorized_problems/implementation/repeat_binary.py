# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    cnt = 0
    s_len = len(s)
    zero_cnt = 0
    
    while True:
        # 0 의 갯수를 세고 0을 기존 문자열에서 제거
        zero_cnt += s.count('0')
        s = s.replace('0','')

        # s의 길이를 이진수화
        s = bin(len(s))[2:]
        cnt += 1
        if s == "1" :
            break
        
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer
