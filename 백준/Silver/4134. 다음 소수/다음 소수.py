import math
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x = int(input())

    k = x
    while True:
        if k > 1:
            is_Prime = True
            for j in range(2, int(k**0.5) + 1):
                if k % j == 0:
                    is_Prime = False
                    break
            if is_Prime:
                print(k)
                break
        k += 1