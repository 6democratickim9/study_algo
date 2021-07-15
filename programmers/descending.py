def solution(n):
    answer=[]
    for i in range(len(str(n))):answer.append(int(str(n)[i]))
    answer.sort(reverse=True)
    return str(answer)
print(solution(118372))
# print(str(i) for i in str(118372))
# for i in str(118363):print (i)
# print(int(str(118637)[1]))