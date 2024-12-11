def solution(s1, s2):
    cnt = 0
    for i in s1:
        for j in s2:
            if i == j:
                cnt += 1
    # len(set(s1) & set(s2))
    return cnt