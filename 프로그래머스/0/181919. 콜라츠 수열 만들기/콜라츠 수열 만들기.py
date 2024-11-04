def solution(n):
    answer = []
    answer.append(n)
    while True:
        if n == 1: 
            break
        if n % 2 == 0:
            n = n // 2
            answer.append(n)
        else:
            n = 3 * n + 1
            answer.append(n)     
    return answer