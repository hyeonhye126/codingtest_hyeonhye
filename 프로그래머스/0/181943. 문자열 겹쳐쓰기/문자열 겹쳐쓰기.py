def solution(my_string, overwrite_string, s):
    answer = ''
    
    for i in range(len(my_string)):
        if i == s:
            for o in overwrite_string:
                answer += o
        elif i < s or s + len(overwrite_string) <= i:
            answer += my_string[i] 
            
    return answer
