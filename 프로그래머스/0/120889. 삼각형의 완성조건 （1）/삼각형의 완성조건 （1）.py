def solution(sides):
    # sides.sort(reverse=True)
    # if sides[0] < sides[1] + sides[2]:
    #     answer = 1
    # else:
    #     answer = 2
    return 1 if max(sides) < sum(sides) - max(sides) else 2