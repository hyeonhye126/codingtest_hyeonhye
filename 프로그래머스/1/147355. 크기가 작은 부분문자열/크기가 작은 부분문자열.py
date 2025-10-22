def solution(t, p):
    answer = 0
    k = len(p)
    
    for i in range(len(t) - k + 1):
        if t[i:i+k] <= p:
            answer += 1
    
    return answer