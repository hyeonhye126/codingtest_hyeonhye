def solution(num, total):    
    i = -100
    
    while True:
        sum_ = 0
        answer = []
        
        for j in range(i, i + num):
            sum_ += j
            answer.append(j)
            
        if sum_ == total:
            break;
        
        i += 1
        
    return answer
