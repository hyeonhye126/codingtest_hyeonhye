def solution(n):
    answer = 0
    for num in list(str(n)):
        answer += int(num)
    return answer