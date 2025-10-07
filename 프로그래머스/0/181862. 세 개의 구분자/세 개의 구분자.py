def solution(myStr):
    answer = []
    tmp = ''
    myS = list(myStr)
    
    for m in myS:
        if m == "a" or m == "b" or m == "c":
            if tmp:
                answer.append(tmp)
                tmp = ''
        else:
            tmp += m
    
    if tmp:
        answer.append(tmp)
    
    if not answer:
        answer.append("EMPTY")
    
    return answer