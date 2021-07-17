def solution(s):
    answer1,answer2=[],[]
    answer1+=(s[i] for i in range(len(s)) if ord(s[i]) in range(97,123))
    answer1.sort(reverse=True)
    answer2+=(s[i] for i in range(len(s)) if ord(s[i]) in range(65,91))
    answer2.sort(reverse=True)
    return ''.join(answer1)+''.join(answer2)


# def solution(s):
#     return ''.join(sorted(s, reverse=True))
#       입력되는 문자열이 알파벳 순으로 입력되는걸 몰랐다.ㅋ
# #  sorted를 사용하면 값이 리스트로 반환되니 ''.join 사용해야 할 듯.
# def solution(s):
#     return sorted(s,reverse=True)
print(solution("Zbcdefg"))