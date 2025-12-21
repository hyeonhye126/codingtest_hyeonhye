def solution(n_str):
    answer = ''
    
    flag = 0
    for i in range(len(n_str)):
        if n_str[i] != "0":
            flag = 1
        if flag == 1:
            answer += n_str[i]
    
    return answer