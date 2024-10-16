#https://school.programmers.co.kr/learn/courses/30/lessons/12924

#등차수열의 합 공식을 활용해 연속된 자연수의 합이 주어진 자연수 n이 되는 경우를 찾는 문제
def solution(n):
    count = 0
    m = 1

    while m * (m - 1) // 2 < n:
        # (n - m * (m - 1) // 2)가 m의 배수인지 확인
        if (n - m * (m - 1) // 2) % m == 0:
            count += 1
        m += 1

    return count


