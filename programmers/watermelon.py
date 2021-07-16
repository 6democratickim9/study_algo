def solution(n):
    if n%2==0:
        return "수박"*(int(n/2))
    else:
        return ("수박"*(int(n/2)))+"수"


# def water_melon(n):
    # return "수박"*(n//2) + "수"*(n%2)
    # 맘에들었던 풀이
print(solution(3))