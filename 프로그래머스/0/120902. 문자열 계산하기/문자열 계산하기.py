def solution(my_string):
    elements = my_string.split()
    
    answer = int(elements[0])
    
    for i in range(1, len(elements), 2):
        operator = elements[i]
        number = int(elements[i + 1])
    
        if operator == '+':
            answer += number
        else:
            answer -= number
    return answer