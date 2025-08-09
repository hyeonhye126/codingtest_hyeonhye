def solution(my_string, indices):
    answer = ''
    index = set(indices)
    
    for i, ch in enumerate(my_string):
        if i not in index:
            answer += ch
    
    return answer