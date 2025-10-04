def solution(myString):
    answer = []
    cnt = -1
    for i in range(len(myString)):
        cnt += 1
        if myString[i] == 'x':
            answer.append(cnt)
            cnt = -1 
    answer.append(cnt+1)
    return answer