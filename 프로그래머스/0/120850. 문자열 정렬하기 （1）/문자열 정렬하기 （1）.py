def solution(my_string):
    answer = []
    for c in my_string:
        if '0' <= c and c <= '9':
            answer.append(int(c))
    answer.sort()
    return answer