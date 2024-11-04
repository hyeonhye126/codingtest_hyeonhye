def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        flag = 0
        if i % 5 == 0:
            for c in str(i):
                if c != '5' and c != '0':
                    flag = 1
            if flag == 0:
                answer.append(i)         
    if not answer:
        answer.append(-1)
    return answer