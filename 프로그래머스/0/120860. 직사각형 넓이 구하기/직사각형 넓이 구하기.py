def solution(dots):
    x, y = [], []
    for c in dots:
        if c[0] not in x:
            x.append(c[0])
        if c[1] not in y:
            y.append(c[1])
    x_ = max(x) - min(x)
    y_ = max(y) - min(y)
    answer = x_ * y_
    return answer