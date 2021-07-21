def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    # 타겟과 numbers가 0이면 1를 반환
    elif not numbers:
        # numbers가 0이면 0 반환
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
        # 재귀함수로 인덱스0 다음부터 끝까지+타겟에서 numbers의 맨앞숫자를 빼고 + 재귀함수로 인덱스0 다음부터 끝까지 타겟에서 numbers의 0을 더한다.

print(solution([1, 1, 1, 1, 1],3))
