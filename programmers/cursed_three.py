def solution(n):
    answer = 0
    no_three_num = 0
    num = 0
    
    while num != n:
        num += 1
        no_three_num += 1
        no_three_num = add_more_numbers(no_three_num)
        
    return no_three_num

def add_more_numbers(no_three_num):
        
    if "3" in str(no_three_num) or no_three_num %3 == 0:
        no_three_num += 1
    else: 
        return no_three_num
    return add_more_numbers(no_three_num)

solution(15)