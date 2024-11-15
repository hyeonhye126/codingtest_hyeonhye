def solution(my_string, letter):
    answer = ''
    for c in my_string:
        if c != letter:
            answer += c
    return answer