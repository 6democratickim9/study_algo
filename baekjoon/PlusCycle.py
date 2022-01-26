o1,o2,n2 = '0','0','0'
ins = input()
cnt = 0
try: 
    o1,o2 = ins[0],ins[1]
    n1,n2 = o1,o2
except: 
    o1 = ins[0]
    n1 = o1
while(True):
    tmp = int(n1)+int(n2)
    tmp = n2+str(tmp)[-1]
    n1,n2 = tmp[0],tmp[1]
    cnt+=1
    if tmp == o1+o2:
        break
    
print(cnt)
    
    

# if(origin == '0'):
#     print(1)
# while(True):
#     # if cnt == 0 :

#     if int(num) < 10:
#         tmp = origin + '0'
#         num = tmp
#         cnt += 1
#             # elif int(num)>=10:
#             #     tmp = int(num[0])+int(num[1])
#             #     tmp = num[1]+str(tmp)[-1]
#             #     num = tmp
#             #     cnt+=1
            
#     elif int(num)>=10:
#         if cnt > 3:
#             if (origin==num) or ('0'+origin==num):
#                 break
#         tmp = str(int(num[0])+int(num[1]))
#         tmp = num[:-1]+tmp[-1]
#         num = tmp
#         cnt+=1

# print(cnt)
