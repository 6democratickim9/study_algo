import sys
input = sys.stdin.readline
a,b=map(int,input().split())

total = a*b
n1,n2,n3,n4,n5=map(int,input().split())
print(-(total-n1),-(total-n2),-(total-n3),-(total-n4),-(total-n5))
# print(type(total-n1)+" "+type(total-n2)+" "+type(total-n3)+" "+type(total-n4)+" "+type(total-n5))   
