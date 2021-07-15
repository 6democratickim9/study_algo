def solution(phonenum):
    return "*"*(len(phonenum)-4)+phonenum[-4:]
print(solution('01033334444'))