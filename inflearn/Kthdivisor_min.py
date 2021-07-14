# import sys
# sys.stdin = open("input.txt", "rt")

param1, param2 = map(int, input().split())
answer = []
if param1 == 0 or param2 == 0:
    print(0)
else:
    for number in range(1, param1+1):
        if param1 % number == 0:
            answer.append(number)

    if len(answer) < param2:
        print(-1)
    else:
        print(answer[param2-1])
