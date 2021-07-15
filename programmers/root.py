import math
def solution(n):
    if (math.sqrt(n))!=int(math.sqrt(n)):
        return -1
    else:
        return (((int(math.sqrt(n)))+1)**2)
print(solution(50000000000000))

# print(str(round(math.sqrt(121),1))[3])
# print(type(str(round(math.sqrt(121),1))[3]))
# print(int(str((round((math.sqrt(1)),1)))[-1:]))
# print(round(1.732339,1))