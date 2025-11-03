from collections import deque # BFS에서 큐 사용

# 1. 입력 받기 
N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점
adj = [[] for _ in range(N + 1)] # 인접 리스트 (정점 번호 1 ~ N)

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a) # 양방향 그래프라서 서로 연결

# 정점 번호가 작은 것부터 방문하도록 정렬
for i in range(1, N + 1):
    adj[i].sort()

# 2. DFS (깊이 우선 탐색)
def dfs(start):
    visited = [False] * (N + 1) # 방문 여부 저장
    stack = [start] # 탐색 시작 노드 스택에 넣기
    order = [] # 방문 순서 기록용
    
    while stack: # 스택이 빌 때까지 반복
        node = stack.pop() # 스택의 마지막 원소 꺼내기
        if visited[node]: 
            continue # 이미 방문했다면 건너뀌기
        visited[node] = True # 방문 처리
        order.append(node) # 방문 순서에 추가

        # 인접 노드 중 방문 안 한 노드들을 "역순"으로 넣기
        # -> 스택은 나중에 넣은 게 먼저 나오므로 역순으로 넣어야 작은 번호부터 방문 가능!
        for next_node in reversed(adj[node]):
            if not visited[next_node]:
                stack.append(next_node)

    print(*order)

# 3. BFS (너비 우선 탐색)
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start]) # 시작 노드를 큐에 넣기
    visited[start] = True
    order = []

    while queue:
        node = queue.popleft() # 큐의 맨앞에서 노드 하나 꺼내기
        order.append(node) # 그 노드를 방문했다고 기록

        for next_node in adj[node]: # 그 노드와 연결된 모든 친구들 탐색
            if not visited[next_node]: # 아직 방문 안했으면
                visited[next_node] = True
                queue.append(next_node) # 다음에 탐색할 노드 추가(큐에 맨 뒤에 넣기)
                
    print(*order)

# 4. 실행
dfs(V)
bfs(V)