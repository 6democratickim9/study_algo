# def solution(pri, loc) :
#     cnt = 1

#     while pri :
#         # print(pri, loc, cnt)
#         maxi = max(pri)
#         node = pri.pop(0)
#         if node == maxi :
#             if loc == 0 : return cnt
#             loc -= 1
#             cnt += 1
#             continue
#         pri.append(node)
#         if loc == 0 :
#             loc = len(pri)-1
#         else :
#             loc -= 1

# print(solution([1,1,9,1,1,1],0))

