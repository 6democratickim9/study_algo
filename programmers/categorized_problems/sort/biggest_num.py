# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    
    # 정수들을 문자열화 한 후에 각 숫자를 3번씩 더한 (666, 101010, 222) 수를 기준으로 내림차순으로 정렬
    # 3번 더한 이유는 numbers 의 원소가 3자리수 까지이기 때문
    numbers = sorted(map(str, numbers), key = lambda x: x*3 , reverse = True)
    answer = ''.join(numbers)
    
    # 0 이 들어간 경우 0 반환
    if answer[0] == '0':
        return '0'
    
    return answer