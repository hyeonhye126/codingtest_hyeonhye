import math

def solution(n):
    sqrt_n = math.sqrt(n)
    
    if sqrt_n == int(sqrt_n):
        return 1
    else:
        return 2