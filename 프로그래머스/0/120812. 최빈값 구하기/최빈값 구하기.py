def solution(array):
    frequency = {}
    
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    highest_frequency = max(frequency.values())
    
    mode = [num for num, freq in frequency.items() if freq == highest_frequency]
    
    if len(mode) > 1:
        answer = -1
    else:
        answer = mode[0]
    
    return answer