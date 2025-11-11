import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for last in range(N - 1, 0, -1):      # last = N-1, N-2, ..., 1
    for i in range(last):             # i = 0 ~ last-1
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]   # swap
            cnt += 1
            if cnt == K:
                print(A[i], A[i + 1])
                sys.exit(0)

print(-1)