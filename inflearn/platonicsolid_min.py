import time
start=time.time()
import sys
sys.stdin = open("input.txt", "rt")
N,M=map(int,sys.stdin.readline().split())
area= (M-N)+1
length=[]
if N==M:
    print (N+1)
else:
    length=list(i+((int(((((N+M)-1)-area))/2))+2) for i in range(0,area))
    for a in length:
        print(a,end=' ')

print("time: ",time.time()-start)


# 그래프를 직접 그려보니 높이 N, 아랫변 길이 M, 가로 총길이(?)(N+M)-1이의 평행사변형이 나옴
# 여기서 중간값을 구하려면 중간에 있는 값의 길이를 알아내고 (평행사변형 안에 있는 직사각형의 가로길이)
# 확률이 높은 숫자들은 직사각형까지 range(가로 길이)해준다
# 영상에 나온 소요시간이 내 코드랑 비슷하게 나왔다. 이유가 궁금하다!