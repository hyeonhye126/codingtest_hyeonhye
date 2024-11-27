def solution(s):
    num_list = []
    for c in s.split():
        if c == 'Z':
            num_list.pop(-1)
        else:
            num_list.append(int(c))
    return sum(num_list)