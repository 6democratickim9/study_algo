from collections import deque  # deque를 사용하기 위해 collections 모듈에서 가져옴

def solution(s):
    # 여는 괄호 '('를 저장할 스택 역할을 할 deque 생성
    open_parentheses = deque()

    # 문자열의 각 문자를 하나씩 순회
    for char in s:
        if char == "(":  
            # 문자가 '('일 경우 스택에 추가
            open_parentheses.append("(")
        elif char == ")":  
            # 문자가 ')'일 경우
            if not open_parentheses:
                # 스택에 '('가 없으면 짝이 맞지 않으므로 False 반환
                return False
            # 스택에 '('가 있으면 해당 괄호를 짝으로 맞추고 pop (제거)
            open_parentheses.pop()

    # 모든 괄호가 짝을 이루었는지 확인 (스택이 비어있으면 True)
    return not open_parentheses  # 스택이 비어있으면 True, 그렇지 않으면 False

