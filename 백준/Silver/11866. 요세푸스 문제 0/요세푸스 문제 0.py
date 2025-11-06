from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))

answer = []
while queue:
    queue.rotate(-(K-1))
    answer.append(queue.popleft())

print('<' + ', '.join(map(str, answer)) + '>')