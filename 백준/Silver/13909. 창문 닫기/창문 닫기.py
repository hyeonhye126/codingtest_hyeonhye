import math
import sys
input = sys.stdin.readline

N = int(input().strip())
print(math.isqrt(N))

# windows = [0] * N

# for i in range (1, N + 1):
#     for idx in range(i, len(windows), i):
#         windows[idx - 1] = 1 - windows[idx - 1]

# print(windows.count(1))