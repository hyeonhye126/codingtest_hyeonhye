def solution(my_string):
    lower_string = my_string.lower()
    answer = ''.join(sorted(lower_string))
    return answer