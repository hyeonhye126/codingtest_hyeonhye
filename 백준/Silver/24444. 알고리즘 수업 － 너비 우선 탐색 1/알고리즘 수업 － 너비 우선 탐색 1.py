from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
order = [0] * (N + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 1
    order[start] = count
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                count += 1
                order[v] = count

bfs(R)

for i in range(1, N + 1):
    print(order[i])