import sys
import math
input = sys.stdin.readline

T = int(input().strip())
Ns = [int(input().strip()) for _ in range(T)]
maxN = max(Ns)

# 1) 에라토스테네스 체 (1번만)
is_prime = [True] * (maxN + 1)
if maxN >= 0:
    is_prime[0] = False
if maxN >= 1:
    is_prime[1] = False

limit = int(math.isqrt(maxN))
for p in range(2, limit + 1):
    if is_prime[p]:
        start = p * p
        is_prime[start:maxN+1:p] = [False] * (((maxN - start) // p) + 1)

# 2) 소수 리스트(2 포함)
primes = [i for i in range(2, maxN + 1) if is_prime[i]]

# 3) 각 케이스 처리: p <= N//2 만 검사
out_lines = []
for N in Ns:
    half = N // 2
    cnt = 0
    for p in primes:
        if p > half:
            break
        if is_prime[N - p]:
            cnt += 1
    out_lines.append(str(cnt))

print("\n".join(out_lines))
