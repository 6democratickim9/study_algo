def solution(s):
    return (s.count('P')+s.count('p')==s.count('y')+s.count('Y'))
print(solution("PpY"))

# def numPY(s):
#     return s.lower().count('p') == s.lower().count('y')
#  한 쪽으로 바꾸고 비교해도 좋다!