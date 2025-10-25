def solution(myString):
    answer = []
    string = list(myString)
    tmp = ''
    
    for s in string:
        if s == "x":
            if tmp:
                answer.append(tmp)
            tmp = ''
        else:
            tmp += s
    
    if tmp:
        answer.append(tmp)
        
    answer.sort()
    return answer