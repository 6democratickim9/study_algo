# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    listed_string = list(s)

# 첫번째로 오는 알파벳의 경우 예외없이 upper()
    if listed_string[0].isalpha():
        listed_string[0] = listed_string[0].upper()

# 인덱스가 0 이상이면서 알파벳, 바로 앞의 문자가 공백인 경우 uppercase, 공백이 아닌 경우 lowercase
    for idx in range(len(listed_string)):
        if idx > 0  and listed_string[idx].isalpha() and listed_string[idx-1] == " " :
            listed_string[idx] = listed_string[idx].upper()
        if idx > 0  and listed_string[idx].isalpha() and listed_string[idx-1] != " " :
            listed_string[idx] = listed_string[idx].lower()
# 정답 string 처리
    answer = ''.join(listed_string)
            
    return answer