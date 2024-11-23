import math

def solution(n):
    i = 2
    while True:
        if math.factorial(i) > n:
             break
        i += 1
    return i - 1