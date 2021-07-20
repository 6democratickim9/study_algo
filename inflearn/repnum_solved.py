# import sys
# sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
ave=round(sum(a)/n)
# round 함수 뒤에 숫자안쓰면 숫자없이 만들어지는군
min=2147000000
# 임시값을 만들어서 순차적으로 비교 후 값 적용
# round는 짝수에 한해 내림이 적용됨. 주의 필요!
for idx,x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave,res)