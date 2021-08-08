import sys
input = sys.stdin.readline
n,song,p=map(int,input().split())
rank=list(map(int,input().split()))
rank.append(song)
rank.sort(reverse=True)
if len(rank)>p and min(rank)>=song:
    print(-1)
else:
    print(rank.index(song)+1)



# 리스트의 길이가 p가 넘어가도 song>min이면 본인 값 프린트하고
# p 안넘으면 무조건 프린트
#딕셔너리로 해주자
