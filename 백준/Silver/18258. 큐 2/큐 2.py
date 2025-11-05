import sys
from collections import deque
input = sys.stdin.readline

def queue_exception():
    print(-1)

N = int(input())
queue = deque()

for i in range(N):
    command = input().split()

    if command[0] == "push":
        x = int(command[1])
        queue.append(x) 
    elif command[0] == "pop":
        if queue:
            top = queue.popleft()
            print(top)
        else:
            queue_exception()
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            queue_exception()
    else:
        if queue:
            print(queue[-1])
        else:
            queue_exception()