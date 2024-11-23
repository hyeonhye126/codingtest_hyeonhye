def solution(my_string):
    mo = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for c in my_string:
        if c not in mo:
            answer += c
    return answer