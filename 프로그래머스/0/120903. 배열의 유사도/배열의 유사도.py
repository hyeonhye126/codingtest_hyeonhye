def solution(s1, s2):
    cnt = 0
    if len(s1) > len(s2):
        for i in s1:
            for j in s2:
                if i == j:
                    cnt += 1
    else:
        for i in s2:
            for j in s1:
                if i == j:
                    cnt += 1
    return cnt