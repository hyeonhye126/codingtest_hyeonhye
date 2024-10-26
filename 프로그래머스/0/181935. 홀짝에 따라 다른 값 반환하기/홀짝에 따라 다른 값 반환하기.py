def solution(n):
    answer = 0
    odd_sum = 0
    even_sum = 0
    
    if n % 2 == 0: # n이 짝수일 때
        for i in range(2, n + 1, 2):
            even_sum += i*i
        answer = even_sum
    else: # n이 홀수일 때
        for i in range(1, n + 1, 2):
            odd_sum += i
        answer = odd_sum
        
    return answer