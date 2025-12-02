import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range (N + 1)]

for _ in range (M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N + 1)
order = 1

def dfs(node):
    global order
    visited[node] = order
    order += 1
    for nxt in graph[node]:
        if visited[nxt] == 0:
            dfs(nxt)

dfs(R) # 시작 정점 넘김

for i in range(1, N + 1):
    print(visited[i])