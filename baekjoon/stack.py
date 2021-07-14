import sys
insert= int(sys.stdin.readline())
command=[]
stack=[]
while insert>0:
    command=sys.stdin.readline().split()
    if command[0]=="push":
        stack.append(int(command[1]))
    elif command[0]=="pop":
        try:
            number=stack.pop()
            print(number)
        except:
            print(-1)
    elif command[0]=="size":
        print(len(stack))
    elif command[0]=="top":
        try:
            print(stack[-1])
        except:
            print(-1)
    elif command[0]=="empty":
        print(int(len(stack)==0))
    insert-=1

#https://www.acmicpc.net/problem/10828