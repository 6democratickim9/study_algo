# import time
# start_time=time.time()
import sys
insert= int(sys.stdin.readline())
tree=[]
for input in range(insert-1):
    tree.append(list(map(int,sys.stdin.readline().split())))
for node in range(2,insert+1):
    for idx in range(0,len(tree)):
        if node==tree[idx][1]:
            print(tree[idx][0])
            break
        elif node==tree[idx][0]:
            print(tree[idx][1])
            break


# end_time=time.time()
# print("time:",end_time-start_time)
# 2 찾을때까지 돌아야댐!!
# 리스트 바뀌는것도 고려하기

    # if str(node) in tree[idx][1]:
    #     print(int(tree[idx][0]))
    #     break
    # elif str(node) in tree[idx][0]:
    #     print(int(tree[idx][1]))
    #     break