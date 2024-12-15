def solution(array):
    cnt = 0
    for ch in str(array):
        for c in ch:
            if c == '7':
                cnt += 1
    return cnt