def solution(s, n):
    store=list(map(str,s))
    for idx in range(len(store)):
        if store[idx] !=' ':
            if ord(store[idx]) in range(97,123):
                if ord(store[idx])+n >122:
                    store[idx]=chr(ord(store[idx])-25+(n-1))
                else:
                    store[idx]=chr(ord(store[idx])+n)
            else:
                if ord(store[idx])+n >90:
                    store[idx]=chr(ord(store[idx])-25+(n-1))
                else:
                    store[idx]=chr(ord(store[idx])+n)
    return ''.join(store)

# def solution(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#             # 대문자면 s[i]를 대문자로 바꾼 뒤 65을 빼준 값에 n을 더하고 난 뒤 해당 값을 26로 나누고 난 나머지값을 A에 더해주고 알파벳으로 바꿔준다.
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)
print(solution("J",25))