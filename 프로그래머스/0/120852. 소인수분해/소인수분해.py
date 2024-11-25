def solution(n):
    answer = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            answer.append(divisor)
            n //= divisor
        else:
            divisor += 1
    answer = sorted(set(answer))
    return answer