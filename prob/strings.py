def solution(s):
    string=''
    answer=''
    words={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for idx in range(len(s)):
        string+=s[idx]
        if string in words:
            answer+=words.get(string)
            string=''
        elif string in words.values():
            answer+=string
            string=''
    
    return int(answer)

print(solution("one4seveneight"))

