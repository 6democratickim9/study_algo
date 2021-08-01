import sys
input = sys.stdin.readline
stu=[]
for a in range(0,5):
    one=int(input())
    if one<40:
        one=40
    stu.append(one)
print(int(sum(stu)/5))