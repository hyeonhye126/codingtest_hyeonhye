def solution(N, stages):
    total = len(stages)
    failure = {}
    
    for i in range(1, N + 1):
        not_clear = stages.count(i) 
        if total == 0:
            failure[i] = 0
        else:
            failure[i] = not_clear / total
        total -= not_clear
        
    sorted_keys = sorted(failure, key=lambda x: (-failure[x], x)) 
    
    return sorted_keys