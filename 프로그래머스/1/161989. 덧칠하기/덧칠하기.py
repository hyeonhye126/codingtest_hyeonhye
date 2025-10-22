def solution(n, m, section):
    answer = 0
    painted = 0
    
    for s in section:
        if painted < s:
            answer += 1
            painted = s + m - 1
    
    return answer