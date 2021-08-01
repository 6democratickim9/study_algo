def solution(record):
    answer = []
    string=''
    id=dict()
    for i in range(len(record)):
        if (record[i].split())[0]=="Leave":
            continue
        else:
            id[((record[i].split())[1])]=((record[i].split())[2])
    for i in range(len(record)):
        if (record[i].split())[0]=="Change":
            continue
        elif (record[i].split())[0]=="Enter":
            string=id[((record[i].split())[1])]+"님이 들어왔습니다."
            answer.append(string)
        elif (record[i].split())[0]=="Leave":
            string=id[((record[i].split())[1])]+"님이 나갔습니다."
            answer.append(string)
    return answer
# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         # rr은 ['Enter','uid1234','Muzi'] 와 같은 형식으로 저장될 것
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]
#         # 딕셔너리 형태의 저장소namespace에 {"uid1234":Muzi}의 형식으로 저장

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             # 앞 부분의 글자가 Change가 아니라면
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
#             # answer에 namespace["uid1234"]의 value+ printer["Enter"]의 value 합치기

#     return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))