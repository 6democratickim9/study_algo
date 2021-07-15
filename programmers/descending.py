def solution(n):
    answer=[]
    for i in range(len(str(n))):answer.append(int(str(n)[i]))
    answer.sort(reverse=True)
    return int("".join([str(_) for _ in answer]))
    # join 이용해서 ""달린 내용들 빼내기
print(solution(118372))
# print(str(i) for i in str(118372))
# for i in str(118363):print (i)
# print(int(str(118637)[1]))