def solution(num):
    strnum = str(num)
    answer = ""
    for idx in range(len(strnum)):

        if strnum[idx] == "1":

            answer += "one"

        if strnum[idx] == "2":
            
            answer += "two"

        if strnum[idx] == "3":
            
            answer += "three" 

        if strnum[idx] == "4":
            
            answer += "four"

        if strnum[idx] == "5":
            
            answer += "five"
    
        if strnum[idx] == "6":
            
            answer += "six"    
    
        if strnum[idx] == "7":
            
            answer += "seven"

        if strnum[idx] == "8":
            
            answer += "eight"    

        if strnum[idx] == "9":
            
            answer += "nine"

        if strnum[idx] == "0":
            
            answer += "zero"
    
    return answer
