def solution(n):
    cnt = 0
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            cnt += 1
            if a != n // a: # (a, b) 인 경우 (b, a) 추가
                cnt += 1
    return cnt