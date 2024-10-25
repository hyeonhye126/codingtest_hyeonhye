def solution(a, b):
    answer = 0
    
    result1 = int(str(a) + str(b))
    result2 = 2 * a * b
    
    if result1 >= result2:
        answer = result1
    else:
        answer = result2
    
    return answer