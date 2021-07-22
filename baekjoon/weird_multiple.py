import sys
A,B= sys.stdin.readline().split()
answer=0
for a in range(len(A)):
    for b in range(len(B)):
        answer+=int(A[a])*int(B[b])
print(answer)

