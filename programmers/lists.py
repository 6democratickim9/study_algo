def solution(arr, divisor):
    arr.sort()
    answer=list(i for i in arr if i%divisor==0)
    if len(answer)==0:
        return [-1]
    return answer


#def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# arr을 돌면서 n이 divisor에 나누어 떨어질 때 n의 값을 저장해서 sorted 하거나 -1를 반환한다.
print(solution([2, 36, 1, 3],10))