def solution(str_list, ex):
    answer = ''
    
    for st in str_list:
        if ex in st:
            continue
        else:
            answer += st
    
    return answer