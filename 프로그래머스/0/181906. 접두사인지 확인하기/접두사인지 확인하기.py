def solution(my_string, is_prefix):
    answer = 0
    l = len(is_prefix)
    
    if is_prefix == my_string[0:l]:
        answer = 1
    else:
        answer = 0
    
    return answer