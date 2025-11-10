from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()
out = []

for i in range(N):
    x = input().split()
    a = x[0]
    
    if a == "push":
        dq.append(x[1])
    elif a == "pop":
        out.append(dq.popleft() if dq else "-1")
    elif a == "size":
        out.append(len(dq))
    elif a == "empty":
        out.append("0" if dq else "1")
    elif a == "front":
        out.append(dq[0] if dq else "-1")
    elif a == "back":
        out.append(dq[-1] if dq else "-1")

for o in out:
    print(o)