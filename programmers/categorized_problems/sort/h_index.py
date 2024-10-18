# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations = sorted(citations)
    
    for idx in range(len(citations)):
        # citations[idx]가 남은 논문 수 (len(citations) - idx)보다 크거나 같으면 H-Index를 만족
        if citations[idx] >= len(citations) - idx:
            return len(citations) - idx
    
    # 만약 해당하는 값이 없으면 H-Index는 0
    return 0

