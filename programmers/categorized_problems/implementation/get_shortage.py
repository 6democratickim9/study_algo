def solution(price, money, count):
    # 총 비용 계산 (등차수열의 합)
    total_cost = price * (count * (count + 1)) // 2
    
    # 모자라는 금액 계산
    shortage = total_cost - money
    
    # 금액이 부족하지 않으면 0을 반환, 그렇지 않으면 부족한 금액 반환
    return max(0, shortage)
