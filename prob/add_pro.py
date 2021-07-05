
def solution(absolutes,signs):
    answer = 0 
    for index in range(len(absolutes)):
        if signs[index]==True:
            answer+= +absolutes[index]
        else:
            answer+= -absolutes[index]
    print(answer)
    return answer


solution()


# from functools import reduce
# def solution(absolutes,signs):
#     answer = []
#     tmp = 0
#     answer = map(lambda x: pass if signs[x]==True else absolutes[x]= range(signs[x]))
#     reduce(lambda x,y:x+y,answer)
# solution([4,7,12],[True,False,True])