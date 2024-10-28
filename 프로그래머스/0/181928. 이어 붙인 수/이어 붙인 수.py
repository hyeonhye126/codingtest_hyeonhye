def solution(num_list):
    odd_sum = ''
    even_sum = ''
    
    for n in num_list:
        if n % 2 != 0:
            odd_sum += str(n)
        else:
            even_sum += str(n)
            
    answer = int(odd_sum) + int(even_sum)
    
    return answer