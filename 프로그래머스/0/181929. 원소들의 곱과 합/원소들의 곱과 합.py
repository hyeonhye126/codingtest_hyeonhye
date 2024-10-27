def solution(num_list):
    num_sum = 0
    num_mul = 1
    
    for n in num_list:
        num_sum += n
        num_mul *= n
    
    if num_mul < (num_sum)**2:
        answer = 1
    else:
        answer = 0

    return answer