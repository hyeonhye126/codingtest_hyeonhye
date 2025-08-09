def solution(my_string):
    answer = []
    
    for c in range(ord('A'), ord('Z') + 1):
        answer.append(my_string.count(chr(c)))
    for c in range(ord('a'), ord('z') + 1):
        answer.append(my_string.count(chr(c)))
    
    return answer