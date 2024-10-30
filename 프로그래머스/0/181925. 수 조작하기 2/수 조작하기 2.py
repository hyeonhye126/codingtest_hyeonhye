def solution(numLog):
    answer = ''

    for i in range(1, len(numLog)):
        tmp = numLog[i] - numLog[i - 1]
        if tmp == 1:
            answer += 'w'
        elif tmp == -1:
            answer += 's'
        elif tmp == 10:
            answer += 'd'
        else:
            answer += 'a'
        
    return answer