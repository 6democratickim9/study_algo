origin = input()
cnt = 0
tmp = num = origin
if(origin == '0'):
    print(1)
while(True):
    # if cnt == 0 :

    if int(num) < 10:
        tmp = origin + '0'
        num = tmp
        cnt += 1
            # elif int(num)>=10:
            #     tmp = int(num[0])+int(num[1])
            #     tmp = num[1]+str(tmp)[-1]
            #     num = tmp
            #     cnt+=1
            
    elif int(num)>=10:
        if cnt > 3:
            if (origin==num) or ('0'+origin==num):
                break
        tmp = str(int(num[0])+int(num[1]))
        tmp = num[:-1]+tmp[-1]
        num = tmp
        cnt+=1

print(cnt)
