import math
def solution(progresses, speeds):
    days = []
    answer = []
    
    for idx in range(len(progresses)):
        days.append(math.ceil((100-progresses[idx])/speeds[idx]))
    days.reverse()


    per=len(days)
    while per>0:
        if len(days)==0:
            break
        per=len(days)
        front=days[len(days)-1]
        if front==max(days):
            answer.append(len(days))
            for roll in range(len(days)):
                days.pop()
        elif front==days[0]:
            answer.append(len(days))
            for roll in range(len(days)):
                days.pop()
        else:
            per=len(days)-1
            for index in range(per,-1,-1):
                if front<days[index]:
                    answer.append(len(days)-(index+1))
                    ran=len(days)-(index+1)
                    for replay in range(0,len(days)-(index+1)):
                        days.pop()
                    break
    return answer
                            

    # per = len(days)
    # while per > 0: #per의 길이가 0보다 클 동안
    #     per = len(days) #days의 길이만큼 per에 저장
    #     if per==0: #per의 길이가 0이면 끝내기
    #         break
    #     if days[per-1]==max(days): 
    #             answer.append(len(days))
    #             for roll in range(len(days)):
    #                 days.pop()
    #     else:
    #         per =len(days)-1
    #         for idx in range(per-1,0,-1):
    #             tmp=days[per-1]
    #             if tmp<days[idx]:
    #                 answer.append(cnt)
    #                 for roll in range(0,cnt):
    #                     days.pop()
    #                 break
    #             elif tmp>days[idx]:
    #                 cnt+=1

    # return answer
##내가 구현하고 싶은 내용
# 맨 앞의 인덱스를 저장해두고, 맨 앞의 인덱스보다 큰 값이 나타나면 
# 해당 값이 나타난 인덱스를 전체 길이에-1 해서 뺀 다음 
# 그 값만큼 돌린다.
# 만약 맨 앞의 인덱스가 제일 크면 해당 리스트의 길이만큼 저장

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([93, 30, 55],[1, 30, 5]))
print(solution([5,5,5],[21,25,20]))

    # - 리스트의 0부터 차례대로 돈다
    #     - 인덱스의 다음 값이 돌고 있는 인덱스보다 크면
    #     인덱스의 값 +1 을 정답 리스트에 저장하고 인덱스를 리스트에서 뺸다.
    #                    if days[idx-1] > days[idx] :
    #                    answer.append(cnt)
     #                   for roll in range(0,cnt):
      #                      days.pop()
       #                 break
        #            if days[idx-1] <= days[idx]:
         #               tmp = days[idx]
          #              if tmp<days[idx-1]:
           #                 answer.append(cnt)
            #                break
    # for com1 in range(len(days)):
    #     cnt=1
    #     for com2 in range(com1+1,len(days)):
    #         if com1+1!=len(days):
    #             if days[com1]>=days[com2]:
    #                 cnt+=1
    #             else:
    #                 answer.append(cnt)
    #                 break
        # for com1 in per:
    #     cnt=1
    #     for com2 in range(1,len(days)):
    #         if days[com1]<days[com2]:
    #             answer.append(cnt)
    #             days.pop(days(com1))
    #         else:
    #             cnt+=1