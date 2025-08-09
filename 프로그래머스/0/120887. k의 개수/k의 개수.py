def solution(i, j, k):
    result = 0
    for x in range(i, j + 1):
        li = list(map(int, str(x)))
        if k in li:
            result += li.count(k)
    return result