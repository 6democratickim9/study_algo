# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    cnt_char = {}
    
    # s 를 돌면서 문자가 없는 경우 -1 담기
    # 있는 경우 현재 인덱스에서 기존 딕셔너리에 있는 문자의 인덱스 빼기
    for s_index in range(len(s)):
        if s[s_index] not in cnt_char:
            answer.append(-1)      
        else:
            answer.append(s_index - cnt_char[s[s_index]])
        cnt_char[s[s_index]] = s_index
    return answer