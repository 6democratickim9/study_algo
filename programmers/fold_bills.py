def solution(wallet, bill):
    cnt = 0
    max_w, min_w = max(wallet), min(wallet)

    # bill 의 최대/최솟값이 wallet 의 최대/최솟값보다 크다면
    # bill 의 max 값을 2로 나눠주고, cnt 를 높여준다
    while max_w < max(bill) or min(bill) > min_w :
        bill[bill.index(max(bill))] = max(bill)//2
        cnt += 1

    return cnt