# def solution(participant, completion):
#     while participant:
#         for com in range(len(completion)):
#             if completion[com] in participant:
#                 participant.pop(participant.index(completion[com]))
#             elif len(participant)==1:
#                 answer=participant[0]
#                 return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx1,idx2 in zip(participant,completion):
        if idx1!=idx2:
            return idx1
    return participant.pop()

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))