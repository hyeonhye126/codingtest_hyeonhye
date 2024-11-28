def solution(order):
    answer = 0
    for c in str(order):
        if c == '3' or c == '6' or c == '9':
            answer += 1
    return answer