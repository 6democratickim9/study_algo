# import sys
# import itertools
# A,B= map(int,(sys.stdin.readline().split()))
# nocombo = []
# types = [i for i in range(1,A+1)]
# result=[]
# type = list(itertools.combinations(types,3))
# result=[]
# for a in range(len(type)):
#     result.append(list(type[a]))

# for _ in range(0,B):
#     tmp=[]
#     n1,n2 = map(int,(sys.stdin.readline().split()))
#     tmp.append(n1)
#     tmp.append(n2)
#     nocombo.append(tmp)

# for x,y in nocombo:
#     cnt=0
#     for idx in range(len(result)):
#         try:
#             if x in result[0] and y in result[0]:
#                 result.remove(result[0])
#                 cnt+=1
#                 continue
#             if x in result[idx-cnt] and y in result[idx-cnt]:
#                 result.remove(result[idx-cnt])
#             else:
#                 continue
#         except:
#             break

# print(len(result))

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N+1)}
    # 딕셔너리로 조합 하면 안되는 값 저장
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, N+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)