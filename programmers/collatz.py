from typing import Counter


def solution(num):
    count=0
    for number in range(500):
        if num==1:
            return count        
        elif num%2==0:
            num=num/2
            count+=1
        elif num%2!=0:
            num=(num*3)+1
            count+=1

    if num!=0:
        return -1

print(solution(6))
print(solution(626331))