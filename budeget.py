# 개쌉구데기코드 다시짤것

# def solution(d, budget):
#     answer = []
#     d.sort()
#     for num,val in enumerate(d):
#         tmp = val
#         cnt = 1
#         and1 = len(d)
#         if val<=budget and len(d)>1:
#             if num!=len(d)-1:
#                 for com in range(num+1, len(d)):
#                     if tmp+d[com]> budget:
#                         answer.append(cnt)
#                         break
#                     elif tmp+d[com]==budget:
#                         cnt+=1
#                         answer.append(cnt)
#                         break
#                     else:
#                         tmp+=d[com]
#                         cnt+=1
#                     answer.append(cnt)
#         elif len(d)<=1:
#             if val>budget:
#                 return 0
#             elif val==budget:
#                 return 1
#             else:
#                 answer.append(cnt)
#     if len(answer) == 0:
#         return 0
#     else:
#         return max(answer)

