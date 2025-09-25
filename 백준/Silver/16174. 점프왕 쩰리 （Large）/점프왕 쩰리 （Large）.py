from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 방문 체크 (무한루프 방지용)
visited = [[False]*N for _ in range(N)]

# BFS를 위한 큐
queue = deque()
queue.append((0, 0)) # 시작점
visited[0][0] = True # 방문 표시
directions = [(0, 1), (1, 0)] # 이동할 수 있는 방향

# 탐색 시작
while queue:
    r, c = queue.popleft()
    step = board[r][c] # 현재 칸의 숫자

    # 목표 도달 체크
    if step == -1:
        print("HaruHaru")
        break

    # 오른쪽, 아래 2가지 방향
    for dr, dc in directions:
        nr, nc = r + dr * step, c + dc * step

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc))

else:
    print("Hing")