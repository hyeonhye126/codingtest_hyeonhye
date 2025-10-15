def solution(s, skip, index):
    skipset = set(skip)
    alpha = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in skipset]
    pos = {ch: i for i, ch in enumerate(alpha)}
    L = len(alpha)
    return ''.join(alpha[(pos[c] + index) % L] for c in s)
