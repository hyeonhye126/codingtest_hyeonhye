def solution(n):
    answer = n
    for i in range(1, n + 1):
        if i % 3 == 0 or '3' in str(i):
            answer += 1
            while answer % 3 == 0 or '3' in str(answer):
                answer += 1
    return answer