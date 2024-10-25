def solution(a, b):
    answer = 0
    
    result1 = int(str(a) + str(b))
    result2 = int(str(b) + str(a))
    
    if result1 > result2:
        answer = result1
    else:
        answer = result2
    
    return answer