def solution(num_list):
    result = 0
    if len(num_list) >= 11:
        for i in range(len(num_list)):
            result += num_list[i]
    else:
        result = 1
        for i in range(len(num_list)):
            result *= num_list[i]
    
    return result