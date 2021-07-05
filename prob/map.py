def solution(n, arr1, arr2):
    tmp=''
    answer=[]
    ans1=[]
    ans2=[]
    for val in range(0,n) :
        ans1.append(bin(arr1[val])[2:].zfill(n))
        ans2.append(bin(arr2[val])[2:].zfill(n))
    
    for place in range(0,n):
        tmp=''
        for idx in range(0,n):
            if int(ans1[place][idx])+int(ans2[place][idx])>=1:
                tmp+='#'
            else:tmp+=' '
        answer.append(tmp)
        
    return answer
