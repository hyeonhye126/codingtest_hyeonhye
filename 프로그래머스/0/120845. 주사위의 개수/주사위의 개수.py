from functools import reduce

def solution(box, n):
    # answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return reduce(lambda x, y: x * y, (box[i] // n for i in range(3)))