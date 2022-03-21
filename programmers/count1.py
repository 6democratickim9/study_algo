def solution(n):
    countInBinN = bin(n).count("1")

    print(countInBinN)

    answer = 0

    for idx in range(1,n):
        if bin(idx).count("1") == countInBinN:
            answer += 1
    
    return answer