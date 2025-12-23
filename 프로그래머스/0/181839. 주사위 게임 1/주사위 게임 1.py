def checknum(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def solution(a, b):
    answer = 0
    
    if checknum(a) == 0 and checknum(b) == 0:
        answer += a**2 + b**2
    elif checknum(a) == 1 and checknum(b) == 1:
        answer += abs(a - b)
    else:
        answer += 2 * (a + b)
    
    return answer