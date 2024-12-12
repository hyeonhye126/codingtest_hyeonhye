def solution(num, k):
    l = list(str(num))
    k = str(k)
    if k in l:
        answer = l.index(k) + 1
    else:
        answer = -1
    return answer