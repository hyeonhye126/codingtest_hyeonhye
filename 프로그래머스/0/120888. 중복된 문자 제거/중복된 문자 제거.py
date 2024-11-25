def solution(my_string):
    answer = []
    answer1 = ''
    for c in my_string:
        if c not in answer:
            answer.append(c)
            answer1 += c
    return answer1