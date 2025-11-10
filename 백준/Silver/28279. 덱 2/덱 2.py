from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()
out = []

for i in range(N):
    x = input().split()
    a = x[0]
    
    if a == "1":
        dq.appendleft(x[1])
    elif a == "2":
        dq.append(x[1])
    elif a == "3":
        out.append(dq.popleft() if dq else "-1")
    elif a == "4":
        out.append(dq.pop() if dq else "-1")
    elif a == "5":
        out.append(len(dq))
    elif a == "6":
        out.append("0" if dq else "1")
    elif a == "7":
        out.append(dq[0] if dq else "-1")
    elif a == "8":
        out.append(dq[-1] if dq else "-1")

for o in out:
    print(o)