from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dq = deque()
for i in range(N):
    if A[i] == 0:
        dq.appendleft(B[i])

M = int(input())
C = list(map(int, input().split()))

res = []
for x in C:
    if dq:
        out = dq.popleft()
        dq.append(x)
    else:
        out = x
    res.append(out)

print(*res)
