import sys
input = sys.stdin.readline
a_digit=input()
a=int(('0b'+input()),2)
b=int(input())
c=2
for i in range(0,b):
    c=c*2
if(a%c==0):
    print("YES")
else:
    print("NO")