from math import prod

def factorial(share):
    return prod(range(1, share + 1))

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer