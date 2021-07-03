def solution(param0):
    answer=[]
    temp=[ ["*"for i in range(5)] for i in range(5)]
    cnt=0
    string=''
    for idx in range(len(param0)):
        cnt+=1
        if cnt%3==0:
            cnt=0
            for idx1 in range(0,idx):
                if temp[(param0[idx-2+idx1])][(param0[idx-1])]!="*":
                    return []
                else: temp[(param0[idx-2+idx1])][(param0[idx-1])]=idx1+1
        
    for j in range(0,5): 
        if sum(temp[i])>=10:
            for i in range(0,5):
                temp[i][j]="*"
    
    for a in range(0,5):
        for b in 
    return answer
print(solution([1,0,4,4,0,2]))