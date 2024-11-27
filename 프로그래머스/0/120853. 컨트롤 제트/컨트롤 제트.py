def solution(s):
    l = s.split(' ')
    l2 = []
    for c in l:
        if c == 'Z':
            l2.pop(-1)
        else:
            l2.append(int(c))
    return sum(l2)