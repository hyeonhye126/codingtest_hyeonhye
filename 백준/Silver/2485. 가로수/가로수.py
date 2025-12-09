import math
import sys
input = sys.stdin.readline

N = int(input())

x = []
for i in range(N):
    x.append(int(input()))

diffs = [x[i+1] - x[i] for i in range(N-1)]

g = diffs[0]
for d in diffs[1:]:
    g = math.gcd(g,d)

total_tree = (x[-1] - x[0]) // g  + 1
print(total_tree - N)