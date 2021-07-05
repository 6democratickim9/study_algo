# def solution(n):
#     answer =''
#     while n>0:
#         n,mod = divmod(n,3)
#         answer+=str(mod)
#     return int(answer,3)

def solution(n):
    return lambda n,mod: divmod(n,3),n
    return map(lambda x,y: (3**x)*y, list(zip(power,nums)))
solution(45)