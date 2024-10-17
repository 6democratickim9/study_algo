from collections import deque

def solution(k, scores):
    score_queue = []
    lowest_score = []
    
    # score 돌아가면서 score_queue 에 넣되 
    # 만약 score_queue의 길이가 3 이상임과 동시에 score_queue min 값보다 큰 경우 min 제거
    # 들어간 자신이 최솟값인 경우 자기 자신 제거
    for score in scores:
        
        score_queue.append(score)
            
        if score > min(score_queue) and len(score_queue) > k:
            min_index = score_queue.index(min(score_queue))
            score_queue.pop(min_index)            
            print(score_queue)
                    
        elif score == min(score_queue) and len(score_queue) > k:
            min_index = score_queue.index(min(score_queue))
            score_queue.pop(min_index)            
            print(score_queue)
            
        lowest_score.append(min(score_queue))
    
    return lowest_score

print(solution(3,[10, 100, 20, 150, 1, 100, 200]))