from collections import deque

N = int(input())
num = list(map(int, input().split()))

queue = deque((i+1, num[i]) for i in range (N))
order = [] # answer

# 시작
idx, k = queue.popleft()
order.append(idx)

while queue:
    if k > 0:
        queue.rotate(-(k-1))
    else:
        queue.rotate(-k)

    idx, k = queue.popleft()
    order.append(idx)

print(*order)