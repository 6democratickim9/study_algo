def solution(numbers):
    unique_sorted_list = list(set(sorted(numbers)))

    # 딕셔너리 형태로 변환 (키: 리스트의 값, 값: 인덱스)
    result_dict = {value: index for index, value in enumerate(unique_sorted_list)}    
        
    answer = []
    return answer