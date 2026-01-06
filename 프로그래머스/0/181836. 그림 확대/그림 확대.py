def solution(picture, k):
    answer = []
    
    for row in picture:
        tmp = ''
        for col in row:
            tmp += col * k
        
        for i in range(k):
            answer.append(tmp)
    
    return answer