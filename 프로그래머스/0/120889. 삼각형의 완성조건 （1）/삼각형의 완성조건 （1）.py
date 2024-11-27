def solution(sides):
    sides.sort(reverse=True)
    if sides[0] < sides[1] + sides[2]:
        answer = 1
    else:
        answer = 2
    return answer